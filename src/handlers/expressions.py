import antlr4
from colorama import Fore, Style
from llvmlite import ir
import re
import sys

from .base import BaseHandler
from primitive import Primitive
from keywords import *

from builder.ProgramNode import ProgramNode

class __ExpressionHandler(BaseHandler):

    def handle_assigmentStmt(self, assignCtx, builder, irFunc, state):
        name = assignCtx.NAME()[0].getText()
        if assignCtx.INTEGER():
            val = assignCtx.INTEGER().getText()
            intPrim = Primitive.int
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
        elif assignCtx.NAME():
            rhName = assignCtx.NAME()[1].getText()  # right hand var name
            rhVal = builder.load(state[rhName])
            if name not in state:
                builder.position_at_start(builder.block)
                state[name] = builder.alloca(rhVal.type, size=1, name=name)
                builder.position_at_end(builder.block)
            builder.store(rhVal, state[name])
        else:
            sys.stderr.write("************** NO ASSIGN FOR YOU *******************")

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
            retVal = self.handle_funcCall(retStmt.funcCall(), builder)
            builder.ret(retVal)
        elif retStmt.NAME():
            varName = retStmt.NAME().getText()
            varPtr = state[varName]
            # result = builder.load(varPtr)
            return builder.ret( builder.load(varPtr) )
        else:
            builder.ret_void()

    def handle_funcCall(self, callCtx, builder):
            callName = callCtx.NAME().getText()

            # TODO - don't make me a special case
            if callName == 'print':
                return self.handle_printFuncCall(callCtx, builder)

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

    def handle_printFuncCall(self, callCtx, builder):
        int8 = ir.IntType(8)
        int32 = ir.IntType(32)

        package = ProgramNode.getPackage('main')

        dataListCtx = callCtx.funcCallDataList().dataList()
        dataList = dataListCtx.data()
        assert(len(dataList) == 1) #  TODO - allow printf varargs

        if dataList[0].NAME():
            text = str(dataList[0].NAME()) + '\n\0' #"foobar\n\0".encode('utf_8')
            text = text.encode('utf_8')
        elif dataList[0].STRING():
            text = str(dataList[0].STRING())[1:-1] + '\n\0' #"foobar\n\0".encode('utf_8')
            text = text.encode('utf_8')

        # text = dataList[0].encode('utf_8')

        size = len(text) + 1

        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(text)),
                                bytearray(text))

        arrayType = ir.ArrayType(int8, len(text))
        glbl = ir.GlobalVariable(package.llvmIR(), arrayType, "tmp_name_1")
        glbl.initializer = c_fmt

        const = [ir.Constant(int32, x) for x in [0, 0]]
        elemPtr = builder.gep(glbl, const, inbounds=True, name='d')
        callFn = package.getFunction('printf').llvmIR()

        result = builder.call(callFn, [elemPtr])


ExpressionHandler = __ExpressionHandler()
