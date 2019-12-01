# Generated from ./Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\60\n\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\6\68\n\6\r\6\16\69\5\6<\n\6\3\6\3\6\3")
        buf.write("\7\7\7A\n\7\f\7\16\7D\13\7\3\b\3\b\5\bH\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\5\nS\n\n\3\13\3\13\3\13\7\13")
        buf.write("X\n\13\f\13\16\13[\13\13\3\f\3\f\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\3\3\2\16\17\2a\2\31\3\2\2\2")
        buf.write("\4\35\3\2\2\2\6\'\3\2\2\2\b-\3\2\2\2\n;\3\2\2\2\fB\3\2")
        buf.write("\2\2\16E\3\2\2\2\20I\3\2\2\2\22M\3\2\2\2\24T\3\2\2\2\26")
        buf.write("\\\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\3\3\2\2\2\35\36\5\6\4\2\36")
        buf.write("\"\7\3\2\2\37!\5\n\6\2 \37\3\2\2\2!$\3\2\2\2\" \3\2\2")
        buf.write("\2\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\4\2\2&\5\3\2\2")
        buf.write("\2\'(\7\5\2\2()\7\16\2\2)*\5\b\5\2*+\7\6\2\2+,\7\24\2")
        buf.write("\2,\7\3\2\2\2-/\7\7\2\2.\60\5\24\13\2/.\3\2\2\2/\60\3")
        buf.write("\2\2\2\60\61\3\2\2\2\61\62\7\b\2\2\62\t\3\2\2\2\63<\5")
        buf.write("\22\n\2\64<\5\16\b\2\65<\5\26\f\2\668\7\16\2\2\67\66\3")
        buf.write("\2\2\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3\2\2\2;\63\3")
        buf.write("\2\2\2;\64\3\2\2\2;\65\3\2\2\2;\67\3\2\2\2<=\3\2\2\2=")
        buf.write(">\7\t\2\2>\13\3\2\2\2?A\5\n\6\2@?\3\2\2\2AD\3\2\2\2B@")
        buf.write("\3\2\2\2BC\3\2\2\2C\r\3\2\2\2DB\3\2\2\2EG\7\n\2\2FH\t")
        buf.write("\2\2\2GF\3\2\2\2GH\3\2\2\2H\17\3\2\2\2IJ\7\16\2\2JK\7")
        buf.write("\13\2\2KL\7\24\2\2L\21\3\2\2\2MN\7\16\2\2NR\7\f\2\2OS")
        buf.write("\7\17\2\2PS\7\16\2\2QS\5\26\f\2RO\3\2\2\2RP\3\2\2\2RQ")
        buf.write("\3\2\2\2S\23\3\2\2\2TY\5\20\t\2UV\7\r\2\2VX\5\20\t\2W")
        buf.write("U\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\25\3\2\2\2[Y")
        buf.write("\3\2\2\2\\]\7\16\2\2]^\7\7\2\2^_\7\b\2\2_\27\3\2\2\2\13")
        buf.write("\33\"/9;BGRY")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'def'", "'->'", "'('", 
                     "')'", "';'", "'return'", "':'", "'='", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'void'", "'int'", "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NAME", "INTEGER", "Newline", "Whitespace", "ALPHANUMERIC", 
                      "SIGN", "VAR_TYPE", "VOID_KW", "INT_KW", "DOUBLE_KW" ]

    RULE_program = 0
    RULE_funcdef = 1
    RULE_signature = 2
    RULE_inputArgs = 3
    RULE_expression = 4
    RULE_expressionList = 5
    RULE_returnStmt = 6
    RULE_typedValue = 7
    RULE_assignment = 8
    RULE_typedValueList = 9
    RULE_funcCall = 10

    ruleNames =  [ "program", "funcdef", "signature", "inputArgs", "expression", 
                   "expressionList", "returnStmt", "typedValue", "assignment", 
                   "typedValueList", "funcCall" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    NAME=12
    INTEGER=13
    Newline=14
    Whitespace=15
    ALPHANUMERIC=16
    SIGN=17
    VAR_TYPE=18
    VOID_KW=19
    INT_KW=20
    DOUBLE_KW=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.FuncdefContext)
            else:
                return self.getTypedRuleContext(MambaParser.FuncdefContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = MambaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.funcdef()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.T__2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def signature(self):
            return self.getTypedRuleContext(MambaParser.SignatureContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MambaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_funcdef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdef" ):
                listener.enterFuncdef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdef" ):
                listener.exitFuncdef(self)




    def funcdef(self):

        localctx = MambaParser.FuncdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_funcdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.signature()
            self.state = 28
            self.match(MambaParser.T__0)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7 or _la==MambaParser.NAME:
                self.state = 29
                self.expression()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(MambaParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignatureContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def inputArgs(self):
            return self.getTypedRuleContext(MambaParser.InputArgsContext,0)


        def VAR_TYPE(self):
            return self.getToken(MambaParser.VAR_TYPE, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_signature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignature" ):
                listener.enterSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignature" ):
                listener.exitSignature(self)




    def signature(self):

        localctx = MambaParser.SignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_signature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(MambaParser.T__2)
            self.state = 38
            self.match(MambaParser.NAME)
            self.state = 39
            self.inputArgs()
            self.state = 40
            self.match(MambaParser.T__3)
            self.state = 41
            self.match(MambaParser.VAR_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedValueList(self):
            return self.getTypedRuleContext(MambaParser.TypedValueListContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_inputArgs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputArgs" ):
                listener.enterInputArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputArgs" ):
                listener.exitInputArgs(self)




    def inputArgs(self):

        localctx = MambaParser.InputArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_inputArgs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MambaParser.T__4)
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME:
                self.state = 44
                self.typedValueList()


            self.state = 47
            self.match(MambaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(MambaParser.AssignmentContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(MambaParser.ReturnStmtContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MambaParser.FuncCallContext,0)


        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(MambaParser.NAME)
            else:
                return self.getToken(MambaParser.NAME, i)

        def getRuleIndex(self):
            return MambaParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = MambaParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 49
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 50
                self.returnStmt()
                pass

            elif la_ == 3:
                self.state = 51
                self.funcCall()
                pass

            elif la_ == 4:
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 52
                    self.match(MambaParser.NAME)
                    self.state = 55 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MambaParser.NAME):
                        break

                pass


            self.state = 59
            self.match(MambaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MambaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = MambaParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7 or _la==MambaParser.NAME:
                self.state = 61
                self.expression()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def INTEGER(self):
            return self.getToken(MambaParser.INTEGER, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)




    def returnStmt(self):

        localctx = MambaParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(MambaParser.T__7)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME or _la==MambaParser.INTEGER:
                self.state = 68
                _la = self._input.LA(1)
                if not(_la==MambaParser.NAME or _la==MambaParser.INTEGER):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def VAR_TYPE(self):
            return self.getToken(MambaParser.VAR_TYPE, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_typedValue

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedValue" ):
                listener.enterTypedValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedValue" ):
                listener.exitTypedValue(self)




    def typedValue(self):

        localctx = MambaParser.TypedValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typedValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MambaParser.NAME)
            self.state = 72
            self.match(MambaParser.T__8)
            self.state = 73
            self.match(MambaParser.VAR_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(MambaParser.NAME)
            else:
                return self.getToken(MambaParser.NAME, i)

        def INTEGER(self):
            return self.getToken(MambaParser.INTEGER, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MambaParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = MambaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(MambaParser.NAME)
            self.state = 76
            self.match(MambaParser.T__9)
            self.state = 80
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 77
                self.match(MambaParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 78
                self.match(MambaParser.NAME)
                pass

            elif la_ == 3:
                self.state = 79
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedValueListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedValue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.TypedValueContext)
            else:
                return self.getTypedRuleContext(MambaParser.TypedValueContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_typedValueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedValueList" ):
                listener.enterTypedValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedValueList" ):
                listener.exitTypedValueList(self)




    def typedValueList(self):

        localctx = MambaParser.TypedValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typedValueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.typedValue()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__10:
                self.state = 83
                self.match(MambaParser.T__10)
                self.state = 84
                self.typedValue()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = MambaParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(MambaParser.NAME)
            self.state = 91
            self.match(MambaParser.T__4)
            self.state = 92
            self.match(MambaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





