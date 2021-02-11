import antlr4
from colorama import Fore, Style
from hashlib import md5
from llvmlite import ir
from llvmlite.ir.instructions import Instruction
from llvmlite.ir.values import Constant
import llvmlite
import re
import sys

from .base import BaseHandler
from primitive import Primitive
from keywords import *

from builder.ProgramNode import ProgramNode
from builder.State import new_scope
from .arithmetic import get_llvmlite_arithmetic_function, get_comparison_operator
from utils import fail_fast

class __ExpressionHandler(BaseHandler):
    __printCnt = 0

    def handle_varDeclare(varDeclareCtx, builder, newScopeObj):
        print("Enter handle_varDeclare")
        sys.stderr.write(f'ERROR - unimplemented handler {handle_varDeclare}')
        sys.exit(6)
        print("Exit handle_varDeclare")

    def handle_declareAndAssignStmt(self, declAndAssignCtx, builder, irFunc, newScopeObj):
        varDeclareCtx = declAndAssignCtx.varDeclare()
        name = varDeclareCtx.NAME().getText()
        isMutable = (varDeclareCtx.MUT() != None)

        package = ProgramNode.getPackage('main')

        currExprCtx = declAndAssignCtx.expression()
        if currExprCtx.makeStructExpr():
            makeStructCtx = currExprCtx.makeStructExpr()
            structName = makeStructCtx.NAME().getText()

            # knownStructDict = package.llvmIR().context.identified_types
            # llvmType = knownStructDict[structName]
            ordElemDict, llvmType = package.getTypeInfo(structName)            
            newScopeObj.allocate(name, builder, llvmType, mutable=isMutable)

            result = self.handle_makeStructExpr(makeStructCtx, builder, newScopeObj)
            newScopeObj.initialize_struct(name, result, ordElemDict, builder)
        else:
            result = self.handle_expression(currExprCtx, builder, newScopeObj)
            newScopeObj.allocate(name, builder, result.type, mutable=isMutable)
            newScopeObj.write(name, result, builder)

    def handle_assigmentStmt(self, assignCtx, builder, irFunc, newScopeObj):
        currExprCtx = assignCtx.expression()
        result = self.handle_expression(currExprCtx, builder, newScopeObj)

        if assignCtx.NAME():
            name = assignCtx.NAME().getText()
            newScopeObj.write(name, result, builder)
        elif assignCtx.field():
            fieldCtx = assignCtx.field()
            package = ProgramNode.getPackage('main')
            fieldNameList = self.get_field_list_for_struct(fieldCtx)
            newScopeObj.write_struct(fieldNameList, result, builder, package)
        else:
            msg = "Could not determine left hand-side af assignment"
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL + '\n')
            sys.exit(5)

    def handle_expression(self, currExprCtx, builder, newScopeObj):
        if currExprCtx.simpleExpression():
            simpExp = currExprCtx.simpleExpression()
            return self.handle_simpleExpr(simpExp, builder, newScopeObj)
        elif currExprCtx.arthimeticExpr():
            arthimeticExprCtx = currExprCtx.arthimeticExpr()
            return self.handle_arthimeticExpr(arthimeticExprCtx, builder, newScopeObj)
        elif currExprCtx.booleanExpression():
            boolExpr = currExprCtx.booleanExpression()
            return self.handle_booleanExpression(boolExpr, builder, newScopeObj)
        elif currExprCtx.makeStructExpr():
            makeStructCtx = currExprCtx.makeStructExpr()
            return self.handle_makeStructExpr(makeStructCtx, builder, newScopeObj)
        else:
            sys.stderr.write("************** NO (DECLARE AND) ASSIGN FOR YOU *******************\n")
            sys.exit(7)

    def handle_bool_atom(self, boolAtomCtx, builder, newScopeObj):
        if boolAtomCtx.simpleBooleanExpression():
            simpBoolExpr = boolAtomCtx.simpleBooleanExpression()
            return self.handle_simpleBooleanExpression(simpBoolExpr, builder, newScopeObj)
        elif boolAtomCtx.booleanExpression():
            boolExpr = boolAtomCtx.booleanExpression()
            return self.handle_booleanExpression(boolExpr, builder, newScopeObj)
        fail_fast("Critical error in handle_bool_atom")

    def handle_andBooleanExpression(self, andBoolCtx, builder, newScopeObj):
        andBooleExprList = andBoolCtx.bool_atom()
        revAtomBoolList = [self.handle_bool_atom(A, builder, newScopeObj) for A in andBooleExprList]
        revAtomBoolList.reverse()

        while len(revAtomBoolList) > 1:
            lhs = revAtomBoolList.pop()
            rhs = revAtomBoolList.pop()
            result = builder.and_(lhs, rhs)
            revAtomBoolList.append(result)
        return revAtomBoolList[0]

    def handle_orBooleanExpression(self, orBoolCtx, builder, newScopeObj):
        andBooleExprList = orBoolCtx.andBooleanExpression()
        revAndBoolList = [self.handle_andBooleanExpression(A, builder, newScopeObj) for A in andBooleExprList]
        revAndBoolList.reverse()

        while len(revAndBoolList) > 1:
            lhs = revAndBoolList.pop()
            rhs = revAndBoolList.pop()
            result = builder.or_(lhs, rhs)
            revAndBoolList.append(result)
        return revAndBoolList[0]

    def handle_booleanExpression(self, boolExprCtx, builder, newScopeObj):
        orCtx = boolExprCtx.orBooleanExpression()
        return self.handle_orBooleanExpression(orCtx, builder, newScopeObj)

        # if boolExprCtx.simpleBooleanExpression():
        #     simpBoolCtxList = boolExprCtx.simpleBooleanExpression()

        #     termResultList = []
        #     for simpBoolCtx in simpBoolCtxList:
        #         termResult = self.handle_simpleBooleanExpression(simpBoolCtx, builder, newScopeObj)
        #         termResultList.append(termResult)

        #     revTermList = termResultList
        #     revBoolOp = boolExprCtx.boolean_comparison_op()
        #     revTermList.reverse()
        #     revBoolOp.reverse()

        #     while revBoolOp:
        #         lhs = revTermList.pop()
        #         rhs = revTermList.pop()
        #         bool_op = revBoolOp.pop()
        #         newTerm = self.resolve_boolean_comparison(lhs, rhs, bool_op, builder)
        #         revTermList.append(newTerm)
        #         # fail_fast("This is not implemented yet")
        #     return revTermList[0]
        # fail_fast("Invalid boolean expression")

    def resolve_boolean_comparison(self, lhs, rhs, bool_op, builder):
        if bool_op.AND():
            return builder.and_(lhs, rhs)
        elif bool_op.OR():
            return builder.or_(lhs, rhs)
        elif bool_op.XOR():
            return builder.xor_(lhs, rhs)
        else:
            fail_fast(f'Unhandled boolean operator -> {bool_op.getText()}')

    def handle_simpleBooleanExpression(self, boolExprCtx, builder, newScopeObj):
        if boolExprCtx.comparisonExpr():
            compExpr = boolExprCtx.comparisonExpr()
            return self.handle_comparisonExpr(compExpr, builder, newScopeObj)
        fail_fast("Invalid simple boolean expression")
      
    def handle_returnStmt(self, retStmt, builder, irFunc, newScopeObj):
        if retStmt.simpleExpression():
            simpleExprCtx = retStmt.simpleExpression()
            retVal = self.handle_simpleExpr(simpleExprCtx, builder, newScopeObj)
            builder.ret(retVal)
        elif retStmt.arthimeticExpr():
            arthimeticExpr = retStmt.arthimeticExpr()
            total = self.handle_arthimeticExpr(arthimeticExpr, builder, newScopeObj)
            return builder.ret(total)
        else:
            builder.ret_void()

    def handle_makeStructExpr(self, makeStructCtx, builder, newScopeObj):
        structName = makeStructCtx.NAME().getText()

        package = ProgramNode.getPackage('main')
        knownStructDict = package.llvmIR().context.identified_types

        if structName not in knownStructDict:
            msg = f'Could not instantiate unknown type {structName}\n'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(3)

        fieldInitList = makeStructCtx.fieldInitList().fieldInit()
        fieldResultList = []
        for field in fieldInitList:
            field_name = field.NAME().getText()
            field_expr_ctx = field.expression()
            field_result = self.handle_expression(field_expr_ctx, builder, newScopeObj)
            fieldResultList.append(field_result)

        llvmType = knownStructDict[structName]
        result = llvmType(fieldResultList)
        return result

    def handle_whileStmt(self, whileCtx, builder, irFunc, newScopeObj):
        uniqId = md5(str(ProgramNode.getPackage('main')).encode()).digest().hex()  # TODO - what if there are multiple packages ?!?
        currBlock = builder.block
        predBlockName = f'predicate.while.{uniqId}'
        entryBlockName = f'entry.while.{uniqId}'
        exitBlockName = f'exit.while.{uniqId}'
        predicateBlock = builder.append_basic_block(name=predBlockName)
        entryBlock = builder.append_basic_block(name=entryBlockName)
        exitBlock = builder.append_basic_block(name=exitBlockName)

        builder.position_at_end(currBlock)
        builder.branch(predicateBlock)

        # check the loop condition
        builder.position_at_start(predicateBlock)
        predicate = self.handle_booleanExpression(whileCtx.booleanExpression(), builder, newScopeObj)
        builder.cbranch(predicate, entryBlock, exitBlock)

        # implement the loop logic here
        builder.position_at_start(entryBlock)
        with new_scope(newScopeObj) as whileScope:
            stmtList = whileCtx.statementList()
            self.handele_statementList(stmtList, builder, irFunc, whileScope)
            builder.branch(predicateBlock)

        # after loop 
        builder.position_at_start(exitBlock)

    def handle_loopStmt(self, loopCtx, builder, irFunc, newScopeObj):
        # print("Entering loop")
        if loopCtx.whileStmt():
            whileCtx = loopCtx.whileStmt()
            self.handle_whileStmt(whileCtx, builder, irFunc, newScopeObj)
        # print("Exitting loop")

    def handle_conditionalStmt(self, conditionalCtx, builder, irFunc, newScopeObj):
        ifCtx = conditionalCtx.ifStmt()
        elifCtxList = conditionalCtx.elifStmt()
        elseCtx = conditionalCtx.elseStmt()
        if not elifCtxList and not elseCtx:
            self.handle_ifStmt(ifCtx, builder, irFunc, newScopeObj)
        elif not elifCtxList:
            self.handle_ifElseStmt(ifCtx, elseCtx, builder, irFunc, newScopeObj)
        else:
            self.handle_ifElifStmt(ifCtx, elifCtxList, elseCtx, builder, irFunc, newScopeObj)

    def handle_ifStmt(self, ifCtx, builder, irFunc, newScopeObj):
        predicate = self.handle_booleanExpression(ifCtx.booleanExpression(), builder, newScopeObj)
        with builder.if_then(predicate): # as (then, otherwise):
            #with then:
                stmtList = ifCtx.statementList()
                self.handele_statementList(stmtList, builder, irFunc, newScopeObj)

    def handle_ifElseStmt(self, ifCtx, elseCtx, builder, irFunc, newScopeObj):
        predicate = self.handle_booleanExpression(ifCtx.booleanExpression(), builder, newScopeObj)
        with builder.if_else(predicate) as (then, otherwise):
            with then:
                stmtList = ifCtx.statementList()
                self.handele_statementList(stmtList, builder, irFunc, newScopeObj)
            with otherwise:
                stmtList = elseCtx.statementList()
                self.handele_statementList(stmtList, builder, irFunc, newScopeObj)

    def handle_ifElifStmt(self, ifCtx, elifCtxList, elseCtx, builder, irFunc, newScopeObj):
        if len(elifCtxList) > 0:
            predicate = self.handle_booleanExpression(ifCtx.booleanExpression(), builder, newScopeObj)
            # recursively calls handle_ifElifStmt inside the 'otherwise' contextmanager
            with builder.if_else(predicate) as (then, otherwise):
                with then:
                    stmtList = ifCtx.statementList()
                    self.handele_statementList(stmtList, builder, irFunc, newScopeObj)
                with otherwise:
                    new_ifCtx = elifCtxList[0]
                    new_elifCtx = [x for (idx, x) in enumerate(elifCtxList) if idx > 0]  # all but the element at idx=0
                    # elseStmt = elseCtx.statementList()
                    self.handle_ifElifStmt(new_ifCtx, new_elifCtx, elseCtx, builder, irFunc, newScopeObj)
        elif elseCtx:
            # this is the base-case for the recursion
            self.handle_ifElseStmt(ifCtx, elseCtx, builder, irFunc, newScopeObj)
        else:
            self.handle_ifStmt(ifCtx, builder, irFunc, newScopeObj)

    def handle_elifStmt(self, elifCtx, builder, irFunc, newScopeObj):
        predicate = self.handle_booleanExpression(ifCtx.booleanExpression(), builder, newScopeObj)
        with builder.if_then(predicate): # as (then, otherwise):
            #with then:
                stmtList = ifCtx.statementList()
                self.handele_statementList(stmtList, builder, irFunc, newScopeObj)

    def handle_funcCall(self, callCtx, builder, newScopeObj):
            callName = callCtx.NAME().getText()

            # TODO - don't make me a special case
            if callName == 'print':
                return self.handle_printFuncCall(callCtx, builder, newScopeObj)

            dataListCtx = callCtx.funcCallDataList().dataList()

            package = ProgramNode.getPackage('main')
            if not dataListCtx:
                callFn = package.getFunction(callName).llvmIR()
                return builder.call(callFn, [])

            dataList = dataListCtx.data()
            callArgs = []
            for dataCtx in dataList:
                if dataCtx.expression():
                    exprCtx = dataCtx.expression()
                    result = self.handle_expression(exprCtx, builder, newScopeObj)
                    callArgs.append(result)
                # elif dataCtx.NAME():
                #     paramName = dataCtx.NAME().getText()
                #     varTypeCtx = newScopeObj.get_type(paramName)
                #     # knownStructDict = package.llvmIR().context.identified_types
                #     # if varTypeCtx.name in knownStructDict:
                #     #     result = newScopeObj.read_struct
                #     #     return
                #     data = newScopeObj.read(paramName, builder)
                #     callArgs.append(data)
                else:
                    msg = f'ERROR: dataCtx has unknown arg type'
                    print(Fore.RED + msg + Style.RESET_ALL)
                    sys.exit(1)

            package = ProgramNode.getPackage('main')
            callFn = package.getFunction(callName).llvmIR()
            result = builder.call(callFn, callArgs)
            return result

    # def handle_multiArthimeticExpr(self, multiArithExpr, builder, newScopeObj):
    #     if multiArithExpr.multiArthimeticExpr():
    #         subMultArithExpr = multiArithExpr.multiArthimeticExpr()
    #         return self.handle_multiArthimeticExpr(subMultArithExpr, builder, newScopeObj)
    #     arthimeticExprList = [A for A in multiArithExpr.arthimeticExpr()]
    #     simpleExpList = [self.handle_arthimeticExpr(expr, builder, newScopeObj) for expr in arthimeticExprList]
    #     arithOpCtx = multiArithExpr.arithmetic_op()
    #     arithOpList = [token for token in arithOpCtx]
    #     return self._arith_from_op_and_term_lists(arithOpList, simpleExpList, builder, newScopeObj)

    def handle_arith_atom(self, arithAtomCtx, builder, newScopeObj):
        if arithAtomCtx.simpleExpression():
            simpleExprCtx = arithAtomCtx.simpleExpression()
            return self.handle_simpleExpr(simpleExprCtx, builder, newScopeObj)
        elif arithAtomCtx.arthimeticExpr():
            arithExprCtx = arithAtomCtx.arthimeticExpr()
            return self.handle_arthimeticExpr(arithExprCtx, builder, newScopeObj)
        fail_fast("unknown error in handle_arith_atom")

    def handle_power(self, powerCtx, builder, newScopeObj):
        revArithOpList = powerCtx.KW_POWER()
        revArithOpList.reverse()

        revAtomList = [self.handle_arith_atom(f, builder, newScopeObj) for f in powerCtx.arith_atom()]
        revAtomList.reverse()

        if len(revAtomList) != (1 + len(revArithOpList)):
            fail_fast("wrong number of factors in handle_term")

        while revArithOpList:
            fail_fast("TODO - handle KW_POWER field in handle_power")
        return revAtomList[0]

    def handle_factor(self, factorCtx, builder, newScopeObj):
        revArithOpList = factorCtx.arith_factor_op()
        revArithOpList.reverse()

        revPowerList = [self.handle_power(f, builder, newScopeObj) for f in factorCtx.power()]
        revPowerList.reverse()

        if len(revPowerList) != (1 + len(revArithOpList)):
            fail_fast("wrong number of factors in handle_term")

        while revArithOpList:
            lhs = revPowerList.pop()
            rhs = revPowerList.pop()
            arithOp = revArithOpList.pop()
            fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)
            result = fn(lhs, rhs)
            revPowerList.append(result)

        return revPowerList[0]

        # arithAtomCtx = factorCtx.arith_atom()
        # if arithAtomCtx:
        #     return self.handle_arith_atom(arithAtomCtx, builder, newScopeObj)

        # numValues = len(factorCtx.simpleExpression())
        # if numValues == 2 and factorCtx.KW_POWER():
        #     fail_fast("TODO - finish me!!!")
        # elif numValues == 1 and factorCtx.KW_POWER() == None:
        #     simpExprCtx = factorCtx.simpleExpression()[0]
        #     result = self.handle_simpleExpr(simpExprCtx, builder, newScopeObj)
        #     return result
        # else:
        #     fail_fast("the power function is malformed")

    def handle_term(self, termCtx, builder, newScopeObj):
        revArithOpList = termCtx.arith_term_op()
        revArithOpList.reverse()

        revFactorList = [self.handle_factor(f, builder, newScopeObj) for f in termCtx.factor()]
        revFactorList.reverse()

        if len(revFactorList) != (1 + len(revArithOpList)):
            fail_fast("wrong number of factors in handle_term")

        while revArithOpList:
            lhs = revFactorList.pop()
            rhs = revFactorList.pop()
            arithOp = revArithOpList.pop()
            fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)
            result = fn(lhs, rhs)
            revFactorList.append(result)

        return revFactorList[0]

    def handle_arthimeticExpr(self, arithExprCtx, builder, newScopeObj):
        termCtx = arithExprCtx.term()
        return self.handle_term(termCtx, builder, newScopeObj)

        # revArithOpList.reverse()

        # revTemList = []
        # subArithList = arithExprCtx.arthimeticExpr()
        # if subArithList:
        #     revTemList = [self.handle_arthimeticExpr(ar, builder, newScopeObj) for ar in subArithList]
        # else:
        #     revTemList = [self.handle_term(t, builder, newScopeObj) for t in arithExprCtx.term()]
        # revTemList.reverse()

        # while revArithOpList:
        #     lhs = revTemList.pop()
        #     rhs = revTemList.pop()
        #     arithOp = revArithOpList.pop()
        #     fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)
        #     result = fn(lhs, rhs)
        #     revTemList.append(result)
        # return revTemList[0]

    def handele_statementList(self, stmtList, builder, irFunc, newScopeObj):
        for exprCtx in stmtList.statement():
            if exprCtx.funcCallStmt():
                # sys.stderr.write("........... Function Call Statement")
                stmtCtx = exprCtx.funcCallStmt()
                self.handle_funcCall(stmtCtx.funcCall(), builder, newScopeObj)

            elif exprCtx.returnStmt():
                # sys.stderr.write("........... Return Statement")
                retStmt = exprCtx.returnStmt()
                self.handle_returnStmt(retStmt, builder, irFunc, newScopeObj)

            elif exprCtx.declareAndAssignStmt():
                declareAndAssignCtx = exprCtx.declareAndAssignStmt()
                self.handle_declareAndAssignStmt(declareAndAssignCtx, builder, irFunc, newScopeObj)

            elif exprCtx.assigmentStmt():
                # sys.stderr.write("........... Assignment Statement")
                assignCtx = exprCtx.assigmentStmt()
                self.handle_assigmentStmt(assignCtx, builder, irFunc, newScopeObj)

            elif exprCtx.conditionalStmt():
                ifCtx = exprCtx.ifStmt()
                self.handle_ifStmt(ifCtx, builder, irFunc, newScopeObj)

            elif exprCtx.loopStmt():
                loopCtx = exprCtx.loopStmt()
                self.handle_loopStmt(loopCtx, builder, irFunc, newScopeObj)
            else:
                sys.stderr.write("........... WTF ?!?\n")
                sys.exit(1)

    def _arith_from_op_and_term_lists(self, arithOpList, simpExpList, builder, newScopeObj):
        if (len(arithOpList) + 1) != len(simpExpList):
            msg = f'Malformed arithmetic expression: {len(arithOpList)} operator and {len(simpExpList)} terms'
            fail_fast(msg)

        if not arithOpList:
            return self.handle_simpleExpr(simpExpList[0], builder, newScopeObj)

        # do multiplication and division
        post_mult_div_simpExpList = []
        post_mult_div_opList = []
        last_op_mult_div = False
        result = None
        for idx, arithOp in enumerate(arithOpList):
            if arithOp.ADD() or arithOp.SUBTRACT():
                # don't do these yet
                if not last_op_mult_div:
                    post_mult_div_simpExpList.append(simpExpList[idx])
                post_mult_div_opList.append(arithOp)
                last_op_mult_div = False
            elif arithOp.MULTIPLY() or arithOp.DIVIDE():
                # handle these now
                if last_op_mult_div:
                    lhs = post_mult_div_simpExpList.pop()
                else:
                    lhs = self.handle_simpleExpr(simpExpList[idx], builder, newScopeObj)
                rhs = self.handle_simpleExpr(simpExpList[idx+1], builder, newScopeObj)
                fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)

                result = fn(lhs, rhs)
                post_mult_div_simpExpList.append(result)

                last_op_mult_div = True
            else:
                msg = 'Unknown arithmetic operator'
                fail_fast(msg)

        if not last_op_mult_div:
            # avoids accidentally dropping the last term
            post_mult_div_simpExpList.append(simpExpList[-1])

        if len(post_mult_div_opList) > 0:
            result = None

        for idx, arithOp in enumerate(post_mult_div_opList):
            # handle these now
            if result:
                lhs = result
            else:
                lhs = self.handle_simpleExpr(post_mult_div_simpExpList[idx], builder, newScopeObj)    # why is this returning a llvmlite.ir.types.PointerType
            rhs = self.handle_simpleExpr(post_mult_div_simpExpList[idx+1], builder, newScopeObj)

            fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)
            result = fn(lhs, rhs)

        # print(post_mult_div_simpExpList)
        # print(post_mult_div_opList)llvmlite.ir.instructions.Instructio
        return result

    def handle_primitive(self, primitiveCtx, builder, newScopeObj):
        if hasattr(primitiveCtx, "numeric") and primitiveCtx.numeric():
            numericCtx = primitiveCtx.numeric()
            return self.handle_numeric(numericCtx, builder, newScopeObj)
        else:
            sys.stderr.write(f'Unknown simpleExpression type for {simpleExpr.getText()}')
            sys.exit(3)

    def handle_numeric(self, numericCtx, builder, newScopeObj):
        package = ProgramNode.getPackage('main')

        if numericCtx.INTEGER():
            irInt = package.get_type_by_name(INT)
            data = numericCtx.INTEGER().getText()
            return irInt(data)
            # return ir.Constant(Primitive.integer, numericCtx.getText())   # TODO - don't assume the numeric() is an Integer
        if numericCtx.DOUBLE():
            irDbl = package.get_type_by_name(DOUBLE)
            data = numericCtx.DOUBLE().getText()
            return irDbl(data)
        else:
            fail_fast(f'Unknown primitive {numericCtx.getText()}')

    # handle a single term from a simpleExpression
    def handle_simpleExpr(self, simpleExpr, builder, newScopeObj):
        if hasattr(simpleExpr, "funcCall") and simpleExpr.funcCall():
            return self.handle_funcCall(simpleExpr.funcCall(), builder, newScopeObj)
        elif hasattr(simpleExpr, "primitive") and simpleExpr.primitive():
            primitiveCtx = simpleExpr.primitive()
            return self.handle_primitive(primitiveCtx, builder, newScopeObj)
        elif hasattr(simpleExpr, "NAME") and simpleExpr.NAME():
            varName = simpleExpr.getText()
            return newScopeObj.read(varName, builder)
        elif hasattr(simpleExpr, "field") and simpleExpr.field():
            fieldCtx = simpleExpr.field()
            result = self.handle_field(fieldCtx, builder, newScopeObj)
            return result
        elif isinstance(simpleExpr, Instruction):
            # TODO .... is this rule too generic to be useful
            return simpleExpr
        elif isinstance(simpleExpr, Constant):
            return simpleExpr
        else:
            sys.stderr.write(f'Unknown simpleExpression type for {simpleExpr.getText()}')
            sys.exit(3)

        sys.stderr.write("handle_simpleExpr reached a point that should be unreachable")

    def get_field_list_for_struct(self, fieldCtx) -> list:
        rootVarName = fieldCtx.NAME().getText()

        fieldNameList = [ rootVarName ]
        for field_ref in fieldCtx.FIELD_REF():
            fieldName = field_ref.getText().lstrip('.')
            fieldNameList.append(fieldName)

        return fieldNameList

    def handle_field(self, fieldCtx, builder, newScopeObj):
        package = ProgramNode.getPackage('main')
        fieldNameList = self.get_field_list_for_struct(fieldCtx)
        return newScopeObj.read_struct(fieldNameList, builder, package)

    def handle_comparisonExpr(self, compExpr, builder, newScopeObj):
        if compExpr.simpleExpression() and len(compExpr.simpleExpression()) == 2:
            simpExpList = compExpr.simpleExpression()
        else:
            sys.stderr.write("arithmetic needs at least 2 simpleExpression")
            sys.exit(3)

        if compExpr.numeric_comparison_op():
            compOpList = [compExpr.numeric_comparison_op()]
        else:
            compOpList = []
            # compOpList.stderr.write("comparison needs at least 1 numeric_comparison_op")
            # sys.exit(3)

        if(len(compOpList) > 1):
            sys.stderr.write(f'Need no more than 1 comparison operator but found {len(compOpList)}')
        if(len(simpExpList) != len(compOpList) + 1):
            sys.stderr.write(f'Need no more than 1 comparison term than operator')

        lhs = self.handle_simpleExpr(simpExpList[0], builder, newScopeObj)
        rhs = self.handle_simpleExpr(simpExpList[1], builder, newScopeObj)
        cmp_op = get_comparison_operator(compOpList[0], builder)
        result =  builder.icmp_signed(cmp_op, lhs, rhs)
        return result

    def handle_printFuncCall(self, callCtx, builder, newScopeObj):
        int8 = ir.IntType(8)
        int32 = ir.IntType(32)

        package = ProgramNode.getPackage('main')

        dataListCtx = callCtx.funcCallDataList().dataList()
        dataList = dataListCtx.data()
        assert(len(dataList) == 1) #  TODO - allow printf varargs

        dataCtx = dataList[0]
        printf_args = []
        if dataCtx.expression() and dataCtx.expression().simpleExpression():
            simpExprCtx = dataCtx.expression().simpleExpression()
            if simpExprCtx.NAME():
                varName = simpExprCtx.NAME().getText()
                varArg = newScopeObj.read(varName, builder)
                printf_args.append(varArg)
                # text = str(newScopeObj.read(varName, builder)) + '\n\0'
                text = '%d\n\0'
                text = text.encode('utf_8')
            elif simpExprCtx.primitive():
                primitiveCtx = simpExprCtx.primitive()
                if primitiveCtx.STRING():
                    text = str(primitiveCtx.STRING())[1:-1] + '\n\0' #"foobar\n\0".encode('utf_8')
                    text = text.encode('utf_8')
                elif primitiveCtx.numeric():
                    numericCtx = primitiveCtx.numeric()
                    text = self.handle_numeric(numericCtx, builder, newScopeObj).get_reference() + '\n\0'
                    text = text.encode('utf_8')
                else:
                    fail_fast('WTF - printout')
        else:
            fail_fast(f'failed print-statment for text "{dataCtx.getText()}"')

        # text = dataList[0].encode('utf_8')

        size = len(text) + 1

        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(text)),
                                bytearray(text))

        arrayType = ir.ArrayType(int8, len(text))
        glbl = ir.GlobalVariable(package.llvmIR(), arrayType, f"print_call_{self.__printCnt}")
        self.__printCnt += 1
        glbl.initializer = c_fmt

        const = [ir.Constant(int32, x) for x in [0, 0]]
        elemPtr = builder.gep(glbl, const, inbounds=True, name='d')
        callFn = package.getFunction('printf').llvmIR()

        result = builder.call(callFn, [elemPtr] + printf_args)


ExpressionHandler = __ExpressionHandler()
