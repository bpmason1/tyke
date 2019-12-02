import antlr4
from llvmlite import ir
import re

from function_table import FunctionTable
from .base import BaseHandler

class __ExpressionHandler(BaseHandler):
    # ExpressionContext
    def handle(self, ctx: antlr4.ParserRuleContext, builder, irFunc):
        # if ctx.funcCall():
        #     print("........... Function Call")
        #     callCtx = ctx.funcCall()
        #     return self.handle_funcCall(callCtx, builder)
        #
        if ctx.returnStmt():
            print("........... Return Statement")
            retStmt = ctx.returnStmt()
            if retStmt.integer():
                val = retStmt.integer().getText()
                irFunc.return_value.type(val)
                retVal = irFunc.return_value.type(val)
                builder.ret(retVal)
            elif retStmt.double():
                val = retStmt.double().getText()
                irFunc.return_value.type(val)
                retVal = irFunc.return_value.type(val)
                builder.ret(retVal)
            else:
                builder.ret_void()
        else:
            print("........... WTF ?!?")
        return

    def handle_funcCall(self, callCtx, builder):
            callName = callCtx.NAME().getText()
            # print( "***************************")
            # print( callCtx.valueList().getChildCount() )
            # print( "***************************")

            if not callCtx.valueList():
                callFn = FunctionTable.getFunction(callName)
                return builder.call(callFn, [])

            param = callCtx.valueList().getChild(0)

            # callArgs = FunctionTable.getFunctionArgs(callName)
            i64 = ir.IntType(64)
            callFn = FunctionTable.getFunction(callName)
            result = builder.call(callFn, [ i64(param) ])
            return result

ExpressionHandler = __ExpressionHandler()
