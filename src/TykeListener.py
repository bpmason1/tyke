# Generated from ./Tyke.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .TykeParser import TykeParser
else:
    from TykeParser import TykeParser

# This class defines a complete listener for a parse tree produced by TykeParser.
class TykeListener(ParseTreeListener):

    # Enter a parse tree produced by TykeParser#program.
    def enterProgram(self, ctx:TykeParser.ProgramContext):
        pass

    # Exit a parse tree produced by TykeParser#program.
    def exitProgram(self, ctx:TykeParser.ProgramContext):
        pass


    # Enter a parse tree produced by TykeParser#package.
    def enterPackage(self, ctx:TykeParser.PackageContext):
        pass

    # Exit a parse tree produced by TykeParser#package.
    def exitPackage(self, ctx:TykeParser.PackageContext):
        pass


    # Enter a parse tree produced by TykeParser#typedef.
    def enterTypedef(self, ctx:TykeParser.TypedefContext):
        pass

    # Exit a parse tree produced by TykeParser#typedef.
    def exitTypedef(self, ctx:TykeParser.TypedefContext):
        pass


    # Enter a parse tree produced by TykeParser#funcdef.
    def enterFuncdef(self, ctx:TykeParser.FuncdefContext):
        pass

    # Exit a parse tree produced by TykeParser#funcdef.
    def exitFuncdef(self, ctx:TykeParser.FuncdefContext):
        pass


    # Enter a parse tree produced by TykeParser#signature.
    def enterSignature(self, ctx:TykeParser.SignatureContext):
        pass

    # Exit a parse tree produced by TykeParser#signature.
    def exitSignature(self, ctx:TykeParser.SignatureContext):
        pass


    # Enter a parse tree produced by TykeParser#ifStmt.
    def enterIfStmt(self, ctx:TykeParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#ifStmt.
    def exitIfStmt(self, ctx:TykeParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#elifStmt.
    def enterElifStmt(self, ctx:TykeParser.ElifStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#elifStmt.
    def exitElifStmt(self, ctx:TykeParser.ElifStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#elseStmt.
    def enterElseStmt(self, ctx:TykeParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#elseStmt.
    def exitElseStmt(self, ctx:TykeParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#conditionalStmt.
    def enterConditionalStmt(self, ctx:TykeParser.ConditionalStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#conditionalStmt.
    def exitConditionalStmt(self, ctx:TykeParser.ConditionalStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#fieldInit.
    def enterFieldInit(self, ctx:TykeParser.FieldInitContext):
        pass

    # Exit a parse tree produced by TykeParser#fieldInit.
    def exitFieldInit(self, ctx:TykeParser.FieldInitContext):
        pass


    # Enter a parse tree produced by TykeParser#fieldInitList.
    def enterFieldInitList(self, ctx:TykeParser.FieldInitListContext):
        pass

    # Exit a parse tree produced by TykeParser#fieldInitList.
    def exitFieldInitList(self, ctx:TykeParser.FieldInitListContext):
        pass


    # Enter a parse tree produced by TykeParser#makeStructExpr.
    def enterMakeStructExpr(self, ctx:TykeParser.MakeStructExprContext):
        pass

    # Exit a parse tree produced by TykeParser#makeStructExpr.
    def exitMakeStructExpr(self, ctx:TykeParser.MakeStructExprContext):
        pass


    # Enter a parse tree produced by TykeParser#whileStmt.
    def enterWhileStmt(self, ctx:TykeParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#whileStmt.
    def exitWhileStmt(self, ctx:TykeParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#loopStmt.
    def enterLoopStmt(self, ctx:TykeParser.LoopStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#loopStmt.
    def exitLoopStmt(self, ctx:TykeParser.LoopStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#breakStmt.
    def enterBreakStmt(self, ctx:TykeParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#breakStmt.
    def exitBreakStmt(self, ctx:TykeParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#continueStmt.
    def enterContinueStmt(self, ctx:TykeParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#continueStmt.
    def exitContinueStmt(self, ctx:TykeParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#branchStmt.
    def enterBranchStmt(self, ctx:TykeParser.BranchStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#branchStmt.
    def exitBranchStmt(self, ctx:TykeParser.BranchStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#statementList.
    def enterStatementList(self, ctx:TykeParser.StatementListContext):
        pass

    # Exit a parse tree produced by TykeParser#statementList.
    def exitStatementList(self, ctx:TykeParser.StatementListContext):
        pass


    # Enter a parse tree produced by TykeParser#statement.
    def enterStatement(self, ctx:TykeParser.StatementContext):
        pass

    # Exit a parse tree produced by TykeParser#statement.
    def exitStatement(self, ctx:TykeParser.StatementContext):
        pass


    # Enter a parse tree produced by TykeParser#returnStmt.
    def enterReturnStmt(self, ctx:TykeParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#returnStmt.
    def exitReturnStmt(self, ctx:TykeParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#funcCallStmt.
    def enterFuncCallStmt(self, ctx:TykeParser.FuncCallStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#funcCallStmt.
    def exitFuncCallStmt(self, ctx:TykeParser.FuncCallStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#declareAndAssignStmt.
    def enterDeclareAndAssignStmt(self, ctx:TykeParser.DeclareAndAssignStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#declareAndAssignStmt.
    def exitDeclareAndAssignStmt(self, ctx:TykeParser.DeclareAndAssignStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#assigmentStmt.
    def enterAssigmentStmt(self, ctx:TykeParser.AssigmentStmtContext):
        pass

    # Exit a parse tree produced by TykeParser#assigmentStmt.
    def exitAssigmentStmt(self, ctx:TykeParser.AssigmentStmtContext):
        pass


    # Enter a parse tree produced by TykeParser#funcDefArgList.
    def enterFuncDefArgList(self, ctx:TykeParser.FuncDefArgListContext):
        pass

    # Exit a parse tree produced by TykeParser#funcDefArgList.
    def exitFuncDefArgList(self, ctx:TykeParser.FuncDefArgListContext):
        pass


    # Enter a parse tree produced by TykeParser#typedArgList.
    def enterTypedArgList(self, ctx:TykeParser.TypedArgListContext):
        pass

    # Exit a parse tree produced by TykeParser#typedArgList.
    def exitTypedArgList(self, ctx:TykeParser.TypedArgListContext):
        pass


    # Enter a parse tree produced by TykeParser#typedArg.
    def enterTypedArg(self, ctx:TykeParser.TypedArgContext):
        pass

    # Exit a parse tree produced by TykeParser#typedArg.
    def exitTypedArg(self, ctx:TykeParser.TypedArgContext):
        pass


    # Enter a parse tree produced by TykeParser#varDeclare.
    def enterVarDeclare(self, ctx:TykeParser.VarDeclareContext):
        pass

    # Exit a parse tree produced by TykeParser#varDeclare.
    def exitVarDeclare(self, ctx:TykeParser.VarDeclareContext):
        pass


    # Enter a parse tree produced by TykeParser#arith_factor_op.
    def enterArith_factor_op(self, ctx:TykeParser.Arith_factor_opContext):
        pass

    # Exit a parse tree produced by TykeParser#arith_factor_op.
    def exitArith_factor_op(self, ctx:TykeParser.Arith_factor_opContext):
        pass


    # Enter a parse tree produced by TykeParser#arith_term_op.
    def enterArith_term_op(self, ctx:TykeParser.Arith_term_opContext):
        pass

    # Exit a parse tree produced by TykeParser#arith_term_op.
    def exitArith_term_op(self, ctx:TykeParser.Arith_term_opContext):
        pass


    # Enter a parse tree produced by TykeParser#arithmetic_op.
    def enterArithmetic_op(self, ctx:TykeParser.Arithmetic_opContext):
        pass

    # Exit a parse tree produced by TykeParser#arithmetic_op.
    def exitArithmetic_op(self, ctx:TykeParser.Arithmetic_opContext):
        pass


    # Enter a parse tree produced by TykeParser#arith_atom.
    def enterArith_atom(self, ctx:TykeParser.Arith_atomContext):
        pass

    # Exit a parse tree produced by TykeParser#arith_atom.
    def exitArith_atom(self, ctx:TykeParser.Arith_atomContext):
        pass


    # Enter a parse tree produced by TykeParser#power.
    def enterPower(self, ctx:TykeParser.PowerContext):
        pass

    # Exit a parse tree produced by TykeParser#power.
    def exitPower(self, ctx:TykeParser.PowerContext):
        pass


    # Enter a parse tree produced by TykeParser#factor.
    def enterFactor(self, ctx:TykeParser.FactorContext):
        pass

    # Exit a parse tree produced by TykeParser#factor.
    def exitFactor(self, ctx:TykeParser.FactorContext):
        pass


    # Enter a parse tree produced by TykeParser#term.
    def enterTerm(self, ctx:TykeParser.TermContext):
        pass

    # Exit a parse tree produced by TykeParser#term.
    def exitTerm(self, ctx:TykeParser.TermContext):
        pass


    # Enter a parse tree produced by TykeParser#arthimeticExpr.
    def enterArthimeticExpr(self, ctx:TykeParser.ArthimeticExprContext):
        pass

    # Exit a parse tree produced by TykeParser#arthimeticExpr.
    def exitArthimeticExpr(self, ctx:TykeParser.ArthimeticExprContext):
        pass


    # Enter a parse tree produced by TykeParser#comparisonExpr.
    def enterComparisonExpr(self, ctx:TykeParser.ComparisonExprContext):
        pass

    # Exit a parse tree produced by TykeParser#comparisonExpr.
    def exitComparisonExpr(self, ctx:TykeParser.ComparisonExprContext):
        pass


    # Enter a parse tree produced by TykeParser#simpleBooleanExpression.
    def enterSimpleBooleanExpression(self, ctx:TykeParser.SimpleBooleanExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#simpleBooleanExpression.
    def exitSimpleBooleanExpression(self, ctx:TykeParser.SimpleBooleanExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#bool_atom.
    def enterBool_atom(self, ctx:TykeParser.Bool_atomContext):
        pass

    # Exit a parse tree produced by TykeParser#bool_atom.
    def exitBool_atom(self, ctx:TykeParser.Bool_atomContext):
        pass


    # Enter a parse tree produced by TykeParser#andBooleanExpression.
    def enterAndBooleanExpression(self, ctx:TykeParser.AndBooleanExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#andBooleanExpression.
    def exitAndBooleanExpression(self, ctx:TykeParser.AndBooleanExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#orBooleanExpression.
    def enterOrBooleanExpression(self, ctx:TykeParser.OrBooleanExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#orBooleanExpression.
    def exitOrBooleanExpression(self, ctx:TykeParser.OrBooleanExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#booleanExpression.
    def enterBooleanExpression(self, ctx:TykeParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#booleanExpression.
    def exitBooleanExpression(self, ctx:TykeParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#boolean_comparison_op.
    def enterBoolean_comparison_op(self, ctx:TykeParser.Boolean_comparison_opContext):
        pass

    # Exit a parse tree produced by TykeParser#boolean_comparison_op.
    def exitBoolean_comparison_op(self, ctx:TykeParser.Boolean_comparison_opContext):
        pass


    # Enter a parse tree produced by TykeParser#numeric_comparison_op.
    def enterNumeric_comparison_op(self, ctx:TykeParser.Numeric_comparison_opContext):
        pass

    # Exit a parse tree produced by TykeParser#numeric_comparison_op.
    def exitNumeric_comparison_op(self, ctx:TykeParser.Numeric_comparison_opContext):
        pass


    # Enter a parse tree produced by TykeParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:TykeParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by TykeParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:TykeParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by TykeParser#numeric.
    def enterNumeric(self, ctx:TykeParser.NumericContext):
        pass

    # Exit a parse tree produced by TykeParser#numeric.
    def exitNumeric(self, ctx:TykeParser.NumericContext):
        pass


    # Enter a parse tree produced by TykeParser#primitive.
    def enterPrimitive(self, ctx:TykeParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by TykeParser#primitive.
    def exitPrimitive(self, ctx:TykeParser.PrimitiveContext):
        pass


    # Enter a parse tree produced by TykeParser#field.
    def enterField(self, ctx:TykeParser.FieldContext):
        pass

    # Exit a parse tree produced by TykeParser#field.
    def exitField(self, ctx:TykeParser.FieldContext):
        pass


    # Enter a parse tree produced by TykeParser#simpleExpression.
    def enterSimpleExpression(self, ctx:TykeParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#simpleExpression.
    def exitSimpleExpression(self, ctx:TykeParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#expression.
    def enterExpression(self, ctx:TykeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TykeParser#expression.
    def exitExpression(self, ctx:TykeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TykeParser#funcCall.
    def enterFuncCall(self, ctx:TykeParser.FuncCallContext):
        pass

    # Exit a parse tree produced by TykeParser#funcCall.
    def exitFuncCall(self, ctx:TykeParser.FuncCallContext):
        pass


    # Enter a parse tree produced by TykeParser#funcCallDataList.
    def enterFuncCallDataList(self, ctx:TykeParser.FuncCallDataListContext):
        pass

    # Exit a parse tree produced by TykeParser#funcCallDataList.
    def exitFuncCallDataList(self, ctx:TykeParser.FuncCallDataListContext):
        pass


    # Enter a parse tree produced by TykeParser#dataList.
    def enterDataList(self, ctx:TykeParser.DataListContext):
        pass

    # Exit a parse tree produced by TykeParser#dataList.
    def exitDataList(self, ctx:TykeParser.DataListContext):
        pass


    # Enter a parse tree produced by TykeParser#data.
    def enterData(self, ctx:TykeParser.DataContext):
        pass

    # Exit a parse tree produced by TykeParser#data.
    def exitData(self, ctx:TykeParser.DataContext):
        pass


    # Enter a parse tree produced by TykeParser#returnType.
    def enterReturnType(self, ctx:TykeParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by TykeParser#returnType.
    def exitReturnType(self, ctx:TykeParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by TykeParser#varType.
    def enterVarType(self, ctx:TykeParser.VarTypeContext):
        pass

    # Exit a parse tree produced by TykeParser#varType.
    def exitVarType(self, ctx:TykeParser.VarTypeContext):
        pass



del TykeParser