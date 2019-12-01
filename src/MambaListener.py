# Generated from ./Mamba.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MambaParser import MambaParser
else:
    from MambaParser import MambaParser

# This class defines a complete listener for a parse tree produced by MambaParser.
class MambaListener(ParseTreeListener):

    # Enter a parse tree produced by MambaParser#program.
    def enterProgram(self, ctx:MambaParser.ProgramContext):
        pass

    # Exit a parse tree produced by MambaParser#program.
    def exitProgram(self, ctx:MambaParser.ProgramContext):
        pass


    # Enter a parse tree produced by MambaParser#funcdef.
    def enterFuncdef(self, ctx:MambaParser.FuncdefContext):
        pass

    # Exit a parse tree produced by MambaParser#funcdef.
    def exitFuncdef(self, ctx:MambaParser.FuncdefContext):
        pass


    # Enter a parse tree produced by MambaParser#signature.
    def enterSignature(self, ctx:MambaParser.SignatureContext):
        pass

    # Exit a parse tree produced by MambaParser#signature.
    def exitSignature(self, ctx:MambaParser.SignatureContext):
        pass


    # Enter a parse tree produced by MambaParser#inputArgs.
    def enterInputArgs(self, ctx:MambaParser.InputArgsContext):
        pass

    # Exit a parse tree produced by MambaParser#inputArgs.
    def exitInputArgs(self, ctx:MambaParser.InputArgsContext):
        pass


    # Enter a parse tree produced by MambaParser#expression.
    def enterExpression(self, ctx:MambaParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MambaParser#expression.
    def exitExpression(self, ctx:MambaParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MambaParser#expressionList.
    def enterExpressionList(self, ctx:MambaParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by MambaParser#expressionList.
    def exitExpressionList(self, ctx:MambaParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by MambaParser#returnStmt.
    def enterReturnStmt(self, ctx:MambaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#returnStmt.
    def exitReturnStmt(self, ctx:MambaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#typedValue.
    def enterTypedValue(self, ctx:MambaParser.TypedValueContext):
        pass

    # Exit a parse tree produced by MambaParser#typedValue.
    def exitTypedValue(self, ctx:MambaParser.TypedValueContext):
        pass


    # Enter a parse tree produced by MambaParser#assignment.
    def enterAssignment(self, ctx:MambaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MambaParser#assignment.
    def exitAssignment(self, ctx:MambaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MambaParser#typedValueList.
    def enterTypedValueList(self, ctx:MambaParser.TypedValueListContext):
        pass

    # Exit a parse tree produced by MambaParser#typedValueList.
    def exitTypedValueList(self, ctx:MambaParser.TypedValueListContext):
        pass


    # Enter a parse tree produced by MambaParser#funcCall.
    def enterFuncCall(self, ctx:MambaParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MambaParser#funcCall.
    def exitFuncCall(self, ctx:MambaParser.FuncCallContext):
        pass


