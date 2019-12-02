import antlr4
from colorama import Fore, Style
from llvmlite import ir
import re
import sys

from function_table import FunctionTable
from .base import BaseHandler
from primitive import Primitive
from keywords import *

class __ExpressionHandler(BaseHandler):
    # ExpressionContext
    def handle(self, ctx: antlr4.ParserRuleContext, builder, irFunc):
        if ctx.funcCallStmt():
            print("........... Function Call Statement")
            stmtCtx = ctx.funcCallStmt()
            return self.handle_funcCall(stmtCtx, builder)

        elif ctx.returnStmt():
            print("........... Return Statement")
            retStmt = ctx.returnStmt()
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
            else:
                builder.ret_void()
        else:
            print("........... WTF ?!?")
        return  None

    def handle_funcCall(self, stmtCtx, builder):
            callCtx = stmtCtx.funcCall()
            callName = callCtx.NAME().getText()

            dataListCtx = callCtx.funcCallDataList().dataList()


            if not dataListCtx:
                callFn = FunctionTable.getFunction(callName)
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

            callFn = FunctionTable.getFunction(callName)
            result = builder.call(callFn, callArgs)
            return result

ExpressionHandler = __ExpressionHandler()
