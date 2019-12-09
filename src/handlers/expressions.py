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
                state[name] = builder.alloca(intPrim, size=1, name=name)
            builder.store(intPrim(val), state[name])
        elif assignCtx.DOUBLE():
            val = assignCtx.DOUBLE().getText()
            doublePrim = Primitive.double
            if name not in state:
                state[name] = builder.alloca(doublePrim, size=1, name=name)
            builder.store(doublePrim(val), state[name])
        elif assignCtx.NAME():
            rhName = assignCtx.NAME()[1].getText()  # right hand var name
            rhVal = builder.load(state[rhName])
            if name not in state:
                state[name] = builder.alloca(rhVal.type, size=1, name=name)
            builder.store(rhVal, state[name])
        else:
            print("************** NO ASSIGN FOR YOU *******************")

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

ExpressionHandler = __ExpressionHandler()
