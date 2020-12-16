# Generated from ./Mamba.g4 by ANTLR 4.9
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


    # Enter a parse tree produced by MambaParser#package.
    def enterPackage(self, ctx:MambaParser.PackageContext):
        pass

    # Exit a parse tree produced by MambaParser#package.
    def exitPackage(self, ctx:MambaParser.PackageContext):
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


    # Enter a parse tree produced by MambaParser#ifStmt.
    def enterIfStmt(self, ctx:MambaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#ifStmt.
    def exitIfStmt(self, ctx:MambaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#elifStmt.
    def enterElifStmt(self, ctx:MambaParser.ElifStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#elifStmt.
    def exitElifStmt(self, ctx:MambaParser.ElifStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#elseStmt.
    def enterElseStmt(self, ctx:MambaParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#elseStmt.
    def exitElseStmt(self, ctx:MambaParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#conditionalStmt.
    def enterConditionalStmt(self, ctx:MambaParser.ConditionalStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#conditionalStmt.
    def exitConditionalStmt(self, ctx:MambaParser.ConditionalStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#whileStmt.
    def enterWhileStmt(self, ctx:MambaParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#whileStmt.
    def exitWhileStmt(self, ctx:MambaParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#loopStmt.
    def enterLoopStmt(self, ctx:MambaParser.LoopStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#loopStmt.
    def exitLoopStmt(self, ctx:MambaParser.LoopStmtContext):
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


    # Enter a parse tree produced by MambaParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:MambaParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:MambaParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#declareAndAssignStmt.
    def enterDeclareAndAssignStmt(self, ctx:MambaParser.DeclareAndAssignStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#declareAndAssignStmt.
    def exitDeclareAndAssignStmt(self, ctx:MambaParser.DeclareAndAssignStmtContext):
        pass


    # Enter a parse tree produced by MambaParser#assigmentStmt.
    def enterAssigmentStmt(self, ctx:MambaParser.AssigmentStmtContext):
        pass

    # Exit a parse tree produced by MambaParser#assigmentStmt.
    def exitAssigmentStmt(self, ctx:MambaParser.AssigmentStmtContext):
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


    # Enter a parse tree produced by MambaParser#varDeclare.
    def enterVarDeclare(self, ctx:MambaParser.VarDeclareContext):
        pass

    # Exit a parse tree produced by MambaParser#varDeclare.
    def exitVarDeclare(self, ctx:MambaParser.VarDeclareContext):
        pass


    # Enter a parse tree produced by MambaParser#arithmetic_op.
    def enterArithmetic_op(self, ctx:MambaParser.Arithmetic_opContext):
        pass

    # Exit a parse tree produced by MambaParser#arithmetic_op.
    def exitArithmetic_op(self, ctx:MambaParser.Arithmetic_opContext):
        pass


    # Enter a parse tree produced by MambaParser#arthimeticExpr.
    def enterArthimeticExpr(self, ctx:MambaParser.ArthimeticExprContext):
        pass

    # Exit a parse tree produced by MambaParser#arthimeticExpr.
    def exitArthimeticExpr(self, ctx:MambaParser.ArthimeticExprContext):
        pass


    # Enter a parse tree produced by MambaParser#multiArthimeticExpr.
    def enterMultiArthimeticExpr(self, ctx:MambaParser.MultiArthimeticExprContext):
        pass

    # Exit a parse tree produced by MambaParser#multiArthimeticExpr.
    def exitMultiArthimeticExpr(self, ctx:MambaParser.MultiArthimeticExprContext):
        pass


    # Enter a parse tree produced by MambaParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:MambaParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by MambaParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:MambaParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by MambaParser#bool_comparison_op.
    def enterBool_comparison_op(self, ctx:MambaParser.Bool_comparison_opContext):
        pass

    # Exit a parse tree produced by MambaParser#bool_comparison_op.
    def exitBool_comparison_op(self, ctx:MambaParser.Bool_comparison_opContext):
        pass


    # Enter a parse tree produced by MambaParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:MambaParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by MambaParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:MambaParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by MambaParser#numeric.
    def enterNumeric(self, ctx:MambaParser.NumericContext):
        pass

    # Exit a parse tree produced by MambaParser#numeric.
    def exitNumeric(self, ctx:MambaParser.NumericContext):
        pass


    # Enter a parse tree produced by MambaParser#simpleExpression.
    def enterSimpleExpression(self, ctx:MambaParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by MambaParser#simpleExpression.
    def exitSimpleExpression(self, ctx:MambaParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by MambaParser#funcCall.
    def enterFuncCall(self, ctx:MambaParser.FuncCallContext):
        pass

    # Exit a parse tree produced by MambaParser#funcCall.
    def exitFuncCall(self, ctx:MambaParser.FuncCallContext):
        pass


    # Enter a parse tree produced by MambaParser#funcCallDataList.
    def enterFuncCallDataList(self, ctx:MambaParser.FuncCallDataListContext):
        pass

    # Exit a parse tree produced by MambaParser#funcCallDataList.
    def exitFuncCallDataList(self, ctx:MambaParser.FuncCallDataListContext):
        pass


    # Enter a parse tree produced by MambaParser#dataList.
    def enterDataList(self, ctx:MambaParser.DataListContext):
        pass

    # Exit a parse tree produced by MambaParser#dataList.
    def exitDataList(self, ctx:MambaParser.DataListContext):
        pass


    # Enter a parse tree produced by MambaParser#data.
    def enterData(self, ctx:MambaParser.DataContext):
        pass

    # Exit a parse tree produced by MambaParser#data.
    def exitData(self, ctx:MambaParser.DataContext):
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



del MambaParser