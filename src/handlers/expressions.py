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

    def handle_assigmentStmt(self, assignCtx, builder, irFunc, state):
        name = assignCtx.NAME()[0].getText()

        # if-else checks type of param for rhs of assignment
        if assignCtx.INTEGER():
            val = assignCtx.INTEGER().getText()
            intPrim = Primitive.integer
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(intPrim, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(intPrim(val), state[name])
        elif assignCtx.DOUBLE():
            val = assignCtx.DOUBLE().getText()
            doublePrim = Primitive.double
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(doublePrim, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(doublePrim(val), state[name])
        elif len(assignCtx.NAME()) > 1:
            # the lhs of the assignment is a NAME so there is always at least 1 NAME regardless of rhs
            rhName = assignCtx.NAME()[1].getText()  # right hand var name
            rhVal = builder.load(state[rhName])
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(rhVal.type, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(rhVal, state[name])
        elif assignCtx.funcCall():
            rhVal = self.handle_funcCall(assignCtx.funcCall(), builder, state)
            if name not in state:
                builder.position_at_start(builder.block)
                if isinstance(rhVal.type, llvmlite.ir.types.DoubleType):
                    state[name] = builder.alloca(Primitive.double, size=1, name=name)
                elif isinstance(rhVal.type, llvmlite.ir.types.IntType):
                    state[name] = builder.alloca(Primitive.integer, size=1, name=name)
                else:
                    sys.stderr.write(f"Unknown function return type {type(rhVal.type)} in assignment")
                builder.position_at_end(builder.block)
            builder.store(rhVal, state[name])
        elif assignCtx.arthimeticExpr():
            arithExpr = assignCtx.arthimeticExpr()
            total = self.handle_arthimeticExpr(arithExpr, builder, state)
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(total.type, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(total, state[name])
        elif assignCtx.multiArthimeticExpr():
            multiArithExpr = assignCtx.multiArthimeticExpr()
            total = self.handle_multiArthimeticExpr(multiArithExpr, builder, state)
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(total.type, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(total, state[name])
        elif assignCtx.comparisonExpr():
            compExpr = assignCtx.comparisonExpr()
            cmpVal = self.handle_comparisonExpr(compExpr, builder, state)
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(Primitive.boolean, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(cmpVal, state[name])
        else:
            sys.stderr.write("************** NO ASSIGN FOR YOU *******************")
            sys.exit(7)

    def handle_returnStmt(self, retStmt, builder, irFunc, state):
        if retStmt.INTEGER():
            val = retStmt.INTEGER().getText()
            irFunc.return_value.type(val)
            retVal = irFunc.return_value.type(val)
            builder.ret(retVal)
        elif retStmt.DOUBLE():
            val = retStmt.DOUBLE().getText()
            irFunc.return_value.type(val)
            retVal = irFunc.return_value.type(val)
            builder.ret(retVal)
        elif retStmt.funcCall():
            retVal = self.handle_funcCall(retStmt.funcCall(), builder, state)
            builder.ret(retVal)
        elif retStmt.NAME():
            varName = retStmt.NAME().getText()
            varPtr = state[varName]
            return builder.ret( builder.load(varPtr) )
        elif retStmt.multiArthimeticExpr():
            multiArithExpr = retStmt.multiArthimeticExpr()
            total = self.handle_multiArthimeticExpr(multiArithExpr, builder, state)
            return builder.ret(total)
        else:
            builder.ret_void()

    def handle_funcCall(self, callCtx, builder, state):
            callName = callCtx.NAME().getText()

            # TODO - don't make me a special case
            if callName == 'print':
                return self.handle_printFuncCall(callCtx, builder, state)

            dataListCtx = callCtx.funcCallDataList().dataList()

            if not dataListCtx:
                package = ProgramNode.getPackage('main')
                callFN = package.getFunction(name).llvmIR()
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

    def handle_multiArthimeticExpr(self, multiArithExpr, builder, state):
        simpleExpList = [self.handle_arthimeticExpr(expr, builder, state) for expr in multiArithExpr.arthimeticExpr()]
        arithOpCtx = multiArithExpr.arithmetic_op()
        arithOpList = [token for token in arithOpCtx]
        return self._arith_from_op_and_term_lists(arithOpList, simpleExpList, builder, state)

    def handle_arthimeticExpr(self, arithExpr, builder, state):
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

        return self._arith_from_op_and_term_lists(arithOpList, simpExpList, builder, state)

    def _arith_from_op_and_term_lists(self, arithOpList, simpExpList, builder, state):
        if (len(arithOpList) + 1) != len(simpExpList):
            sys.stderr.write(f'Malformed arithmetic expression: {len(arithOpList)} operator and {len(simpExpList)} terms')
            sys.exit(3)

        if not arithOpList:
            return self.handle_simpleExpr(simpExpList[0], builder, state)

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
                    lhs = self.handle_simpleExpr(simpExpList[idx], builder, state)
                rhs = self.handle_simpleExpr(simpExpList[idx+1], builder, state)
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
                lhs = self.handle_simpleExpr(post_mult_div_simpExpList[idx], builder, state)
            rhs = self.handle_simpleExpr(post_mult_div_simpExpList[idx+1], builder, state)

            fn = get_llvmlite_arithmetic_function(lhs.type, arithOp, builder)
            result = fn(lhs, rhs)

        # print(post_mult_div_simpExpList)
        # print(post_mult_div_opList)llvmlite.ir.instructions.Instructio
        return result

    # handle a single term from a simpleExpression
    def handle_simpleExpr(self, simpleExpr, builder, state):
        if hasattr(simpleExpr, "funcCall") and simpleExpr.funcCall():
            return self.handle_funcCall(simpleExpr.funcCall(), builder, state)
        elif hasattr(simpleExpr, "numeric") and simpleExpr.numeric():
            return ir.Constant(Primitive.integer, simpleExpr.numeric().getText())
        elif hasattr(simpleExpr, "NAME") and simpleExpr.NAME():
            stackPtr = state[simpleExpr.getText()]
            return builder.load(stackPtr)
        elif isinstance(simpleExpr, Instruction):
            # TODO .... is this rule too generic to be useful
            return simpleExpr
        elif isinstance(simpleExpr, Constant):
            return simpleExpr
        else:
            sys.stderr.write('Unknown simpleExpression type for {simpleExpr.getText()}')
            sys.exit(3)

        sys.stderr.write("handle_simpleExpr reached a point that should be unreachable")

    def handle_comparisonExpr(self, compExpr, builder, state):
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

        lhs = self.handle_simpleExpr(simpExpList[0], builder, state)
        rhs = self.handle_simpleExpr(simpExpList[1], builder, state)
        cmp_op = get_comparison_operator(compOpList[0], builder)
        result =  builder.icmp_signed(cmp_op, lhs, rhs)
        return result

    def handle_printFuncCall(self, callCtx, builder, state):
        int8 = ir.IntType(8)
        int32 = ir.IntType(32)

        package = ProgramNode.getPackage('main')

        dataListCtx = callCtx.funcCallDataList().dataList()
        dataList = dataListCtx.data()
        assert(len(dataList) == 1) #  TODO - allow printf varargs

        if dataList[0].NAME():
            varName = dataList[0].NAME().getText()
            # print(type(state['xxx']))
            # print(dir(state['xxx']))
            text = str(state[varName]) + '\n\0'
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
