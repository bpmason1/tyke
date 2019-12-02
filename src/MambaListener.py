# Generated from Mamba.g4 by ANTLR 4.7.2
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


    # Enter a parse tree produced by MambaParser#statementList.
    def enterStatementList(self, ctx:MambaParser.StatementListContext):
        pass

    # Exit a parse tree produced by MambaParser#statementList.
    def exitStatementList(self, ctx:MambaParser.StatementListContext):
        pass


    # Enter a parse tree produced by MambaParser#statement.
    def enterStatement(self, ctx:MambaParser.StatementContext):
        pass

    # Exit a parse tree produced by MambaParser#statement.
    def exitStatement(self, ctx:MambaParser.StatementContext):
        pass


    # Enter a parse tree produced by MambaParser#returnStmt.
    def enterReturnStmt(self, ctx:MambaParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#returnStmt.
    def exitReturnStmt(self, ctx:MambaParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#funcDefArgList.
    def enterFuncDefArgList(self, ctx:MambaParser.FuncDefArgListContext):
        pass

    # Exit a parse tree produced by MambaParser#funcDefArgList.
    def exitFuncDefArgList(self, ctx:MambaParser.FuncDefArgListContext):
        pass


    # Enter a parse tree produced by MambaParser#typedArgList.
    def enterTypedArgList(self, ctx:MambaParser.TypedArgListContext):
        pass

    # Exit a parse tree produced by MambaParser#typedArgList.
    def exitTypedArgList(self, ctx:MambaParser.TypedArgListContext):
        pass


    # Enter a parse tree produced by MambaParser#typedArg.
    def enterTypedArg(self, ctx:MambaParser.TypedArgContext):
        pass

    # Exit a parse tree produced by MambaParser#typedArg.
    def exitTypedArg(self, ctx:MambaParser.TypedArgContext):
        pass


    # Enter a parse tree produced by MambaParser#double.
    def enterDouble(self, ctx:MambaParser.DoubleContext):
        pass

    # Exit a parse tree produced by MambaParser#double.
    def exitDouble(self, ctx:MambaParser.DoubleContext):
        pass


    # Enter a parse tree produced by MambaParser#integer.
    def enterInteger(self, ctx:MambaParser.IntegerContext):
        pass

    # Exit a parse tree produced by MambaParser#integer.
    def exitInteger(self, ctx:MambaParser.IntegerContext):
        pass


    # Enter a parse tree produced by MambaParser#name.
    def enterName(self, ctx:MambaParser.NameContext):
        pass

    # Exit a parse tree produced by MambaParser#name.
    def exitName(self, ctx:MambaParser.NameContext):
        pass


    # Enter a parse tree produced by MambaParser#returnType.
    def enterReturnType(self, ctx:MambaParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by MambaParser#returnType.
    def exitReturnType(self, ctx:MambaParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by MambaParser#varType.
    def enterVarType(self, ctx:MambaParser.VarTypeContext):
        pass

    # Exit a parse tree produced by MambaParser#varType.
    def exitVarType(self, ctx:MambaParser.VarTypeContext):
        pass


