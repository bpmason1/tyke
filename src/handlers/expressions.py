import antlr4
from colorama import Fore, Style
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
from .arithmetic import get_llvmlite_arithmetic_function, get_comparison_operator

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

        if declAndAssignCtx.simpleExpression():
            simpExp = declAndAssignCtx.simpleExpression()
            result = self.handle_simpleExpr(simpExp, builder, newScopeObj)
            newScopeObj.allocate(name, builder, result.type, mutable=isMutable)
            newScopeObj.write(name, result, builder)
        elif declAndAssignCtx.arthimeticExpr():
            arithExpr = declAndAssignCtx.arthimeticExpr()
            result = self.handle_arthimeticExpr(arithExpr, builder, newScopeObj)
            newScopeObj.allocate(name, builder, result.type, mutable=isMutable)
            newScopeObj.write(name, result, builder)
        elif declAndAssignCtx.multiArthimeticExpr():
            multiArithExpr = declAndAssignCtx.multiArthimeticExpr()
            result = self.handle_multiArthimeticExpr(multiArithExpr, builder, newScopeObj)
            newScopeObj.allocate(name, builder, result.type, mutable=isMutable)
            newScopeObj.write(name, result, builder)
        elif declAndAssignCtx.comparisonExpr():
            compExpr = declAndAssignCtx.comparisonExpr()
            result = self.handle_comparisonExpr(compExpr, builder, newScopeObj)
            newScopeObj.allocate(name, builder, result.type, mutable=isMutable)
            newScopeObj.write(name, result, builder)
        else:
            sys.stderr.write("************** NO DECLARE AND ASSIGN FOR YOU *******************\n")
            sys.exit(7)

    def handle_assigmentStmt(self, assignCtx, builder, irFunc, newScopeObj):
        name = assignCtx.NAME().getText()

        if assignCtx.simpleExpression():
            simpExp = assignCtx.simpleExpression()
            result = self.handle_simpleExpr(simpExp, builder, newScopeObj)
            newScopeObj.write(name, result, builder)
        elif assignCtx.arthimeticExpr():
            arithExpr = assignCtx.arthimeticExpr()
            result = self.handle_arthimeticExpr(arithExpr, builder, newScopeObj)
            newScopeObj.write(name, result, builder)
        elif assignCtx.multiArthimeticExpr():
            multiArithExpr = assignCtx.multiArthimeticExpr()
            result = self.handle_multiArthimeticExpr(multiArithExpr, builder, newScopeObj)
            newScopeObj.write(name, result, builder)
        elif assignCtx.comparisonExpr():
            compExpr = assignCtx.comparisonExpr()
            result = self.handle_comparisonExpr(compExpr, builder, newScopeObj)
            newScopeObj.write(name, result, builder)
        else:
            sys.stderr.write("************** NO DECLARE AND ASSIGN FOR YOU *******************\n")
            sys.exit(7)

    def handle_returnStmt(self, retStmt, builder, irFunc, newScopeObj):
        if retStmt.simpleExpression():
            simpleExprCtx = retStmt.simpleExpression()
            retVal = self.handle_simpleExpr(simpleExprCtx, builder, newScopeObj)
            builder.ret(retVal)
        elif retStmt.multiArthimeticExpr():
            multiArithExpr = retStmt.multiArthimeticExpr()
            total = self.handle_multiArthimeticExpr(multiArithExpr, builder, newScopeObj)
            return builder.ret(total)
        else:
            builder.ret_void()

    def handle_ifStmt(self, ifCtx, builder, irFunc, newScopeObj):
        predicate = self.handle_comparisonExpr(ifCtx.comparisonExpr(), builder, newScopeObj)
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

            if not dataListCtx:
                package = ProgramNode.getPackage('main')
                callFn = package.getFunction(callName).llvmIR()
                return builder.call(callFn, [])

            dataList = dataListCtx.data()
            callArgs = []
            for dataCtx in dataList:

                if dataCtx.INTEGER():
                    irInt = Primitive.get_type_by_name(INT)
                    data = dataCtx.INTEGER().getText()
                    callArgs.append(irInt(data))
                elif dataCtx.DOUBLE():
                    irDbl = Primitive.get_type_by_name(DOUBLE)
                    data = dataCtx.DOUBLE().getText()
                    callArgs.append(irDbl(data))
                else:
                    msg = f'ERROR: dataCtx has unknown arg type'
                    print(Fore.RED + msg + Style.RESET_ALL)
                    sys.exit(1)

            package = ProgramNode.getPackage('main')
            callFn = package.getFunction(callName).llvmIR()
            result = builder.call(callFn, callArgs)
            return result

    def handle_multiArthimeticExpr(self, multiArithExpr, builder, newScopeObj):
        arthimeticExprList = [A for A in multiArithExpr.arthimeticExpr()]
        simpleExpList = [self.handle_arthimeticExpr(expr, builder, newScopeObj) for expr in arthimeticExprList]
        arithOpCtx = multiArithExpr.arithmetic_op()
        arithOpList = [token for token in arithOpCtx]
        return self._arith_from_op_and_term_lists(arithOpList, simpleExpList, builder, newScopeObj)

    def handle_arthimeticExpr(self, arithExpr, builder, newScopeObj):
        if arithExpr.simpleExpression():
            simpExpList = [token for token in arithExpr.simpleExpression()]
        else:
            sys.stderr.write("arithmetic needs at least 2 simpleExpression")
            sys.exit(3)

        if arithExpr.arithmetic_op():
            arithOpCtx = arithExpr.arithmetic_op()
            arithOpList = [token for token in arithOpCtx]
        else:
            arithOpList = []
            # sys.stderr.write("arithmetic needs at least 1 arithmetic_op")
            # sys.exit(3)

        return self._arith_from_op_and_term_lists(arithOpList, simpExpList, builder, newScopeObj)

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

            elif exprCtx.assigmentStmt():
                # sys.stderr.write("........... Assignment Statement")
                assignCtx = exprCtx.assigmentStmt()
                self.handle_assigmentStmt(assignCtx, builder, irFunc, newScopeObj)
            elif exprCtx.ifStmt():
                ifCtx = exprCtx.ifStmt()
                self.handle_ifStmt(ifCtx, builder, irFunc, newScopeObj)
            else:
                sys.stderr.write("........... WTF ?!?\n")
                sys.exit(1)

    def _arith_from_op_and_term_lists(self, arithOpList, simpExpList, builder, newScopeObj):
        if (len(arithOpList) + 1) != len(simpExpList):
            sys.stderr.write(f'Malformed arithmetic expression: {len(arithOpList)} operator and {len(simpExpList)} terms')
            sys.exit(3)

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
                sys.stderr.write(f'Unknown arithmetic operator')
                sys.exit(3)

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

    # handle a single term from a simpleExpression
    def handle_simpleExpr(self, simpleExpr, builder, newScopeObj):
        if hasattr(simpleExpr, "funcCall") and simpleExpr.funcCall():
            return self.handle_funcCall(simpleExpr.funcCall(), builder, newScopeObj)
        elif hasattr(simpleExpr, "numeric") and simpleExpr.numeric():
            return ir.Constant(Primitive.integer, simpleExpr.numeric().getText())   # TODO - don't assume the numeric() is an Integer
        elif hasattr(simpleExpr, "NAME") and simpleExpr.NAME():
            varName = simpleExpr.getText()
            return newScopeObj.read(varName, builder)
        elif isinstance(simpleExpr, Instruction):
            # TODO .... is this rule too generic to be useful
            return simpleExpr
        elif isinstance(simpleExpr, Constant):
            return simpleExpr
        else:
            sys.stderr.write('Unknown simpleExpression type for {simpleExpr.getText()}')
            sys.exit(3)

        sys.stderr.write("handle_simpleExpr reached a point that should be unreachable")

    def handle_comparisonExpr(self, compExpr, builder, newScopeObj):
        if compExpr.simpleExpression() and len(compExpr.simpleExpression()) == 2:
            simpExpList = compExpr.simpleExpression()
        else:
            sys.stderr.write("arithmetic needs at least 2 simpleExpression")
            sys.exit(3)

        if compExpr.bool_comparison_op():
            compOpList = [compExpr.bool_comparison_op()]
        else:
            compOpList = []
            # compOpList.stderr.write("comparison needs at least 1 bool_comparison_op")
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

        if dataList[0].NAME():
            varName = dataList[0].NAME().getText()
            text = str(newScopeObj.read(varName, builder)) + '\n\0'
            text = text.encode('utf_8')
        elif dataList[0].STRING():
            text = str(dataList[0].STRING())[1:-1] + '\n\0' #"foobar\n\0".encode('utf_8')
            text = text.encode('utf_8')
        else:
            print(dir(dataList[0]))

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

        result = builder.call(callFn, [elemPtr])


ExpressionHandler = __ExpressionHandler()
