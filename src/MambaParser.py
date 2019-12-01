# Generated from Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("p\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\6\2")
        buf.write("\34\n\2\r\2\16\2\35\3\3\3\3\3\3\7\3#\n\3\f\3\16\3&\13")
        buf.write("\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5\5\62\n\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\6\6:\n\6\r\6\16\6;\5\6>\n\6\3")
        buf.write("\6\3\6\3\7\7\7C\n\7\f\7\16\7F\13\7\3\b\3\b\3\b\3\b\5\b")
        buf.write("L\n\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\5\nW\n\n\3\13")
        buf.write("\3\13\3\13\7\13\\\n\13\f\13\16\13_\13\13\3\f\3\f\3\f\7")
        buf.write("\fd\n\f\f\f\16\fg\13\f\3\r\3\r\3\r\5\rl\n\r\3\r\3\r\3")
        buf.write("\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\2\2s\2\33\3")
        buf.write("\2\2\2\4\37\3\2\2\2\6)\3\2\2\2\b/\3\2\2\2\n=\3\2\2\2\f")
        buf.write("D\3\2\2\2\16G\3\2\2\2\20M\3\2\2\2\22Q\3\2\2\2\24X\3\2")
        buf.write("\2\2\26`\3\2\2\2\30h\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2")
        buf.write("\2\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\3\3\2")
        buf.write("\2\2\37 \5\6\4\2 $\7\3\2\2!#\5\n\6\2\"!\3\2\2\2#&\3\2")
        buf.write("\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\4")
        buf.write("\2\2(\5\3\2\2\2)*\7\5\2\2*+\7\17\2\2+,\5\b\5\2,-\7\6\2")
        buf.write("\2-.\7\25\2\2.\7\3\2\2\2/\61\7\7\2\2\60\62\5\24\13\2\61")
        buf.write("\60\3\2\2\2\61\62\3\2\2\2\62\63\3\2\2\2\63\64\7\b\2\2")
        buf.write("\64\t\3\2\2\2\65>\5\22\n\2\66>\5\16\b\2\67>\5\30\r\28")
        buf.write(":\7\17\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<>\3")
        buf.write("\2\2\2=\65\3\2\2\2=\66\3\2\2\2=\67\3\2\2\2=9\3\2\2\2>")
        buf.write("?\3\2\2\2?@\7\t\2\2@\13\3\2\2\2AC\5\n\6\2BA\3\2\2\2CF")
        buf.write("\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\r\3\2\2\2FD\3\2\2\2GK\7")
        buf.write("\n\2\2HL\7\17\2\2IL\7\20\2\2JL\5\30\r\2KH\3\2\2\2KI\3")
        buf.write("\2\2\2KJ\3\2\2\2KL\3\2\2\2L\17\3\2\2\2MN\7\17\2\2NO\7")
        buf.write("\13\2\2OP\7\25\2\2P\21\3\2\2\2QR\7\17\2\2RV\7\f\2\2SW")
        buf.write("\7\20\2\2TW\7\17\2\2UW\5\30\r\2VS\3\2\2\2VT\3\2\2\2VU")
        buf.write("\3\2\2\2W\23\3\2\2\2X]\5\20\t\2YZ\7\r\2\2Z\\\5\20\t\2")
        buf.write("[Y\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\25\3\2\2\2")
        buf.write("_]\3\2\2\2`e\7\16\2\2ab\7\r\2\2bd\7\16\2\2ca\3\2\2\2d")
        buf.write("g\3\2\2\2ec\3\2\2\2ef\3\2\2\2f\27\3\2\2\2ge\3\2\2\2hi")
        buf.write("\7\17\2\2ik\7\7\2\2jl\5\26\f\2kj\3\2\2\2kl\3\2\2\2lm\3")
        buf.write("\2\2\2mn\7\b\2\2n\31\3\2\2\2\r\35$\61;=DKV]ek")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'def'", "'->'", "'('", 
                     "')'", "';'", "'return'", "':'", "'='", "','", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'void'", "'int'", 
                     "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SCALAR", "NAME", "INTEGER", "Newline", "Whitespace", 
                      "ALPHANUMERIC", "SIGN", "VAR_TYPE", "VOID_KW", "INT_KW", 
                      "DOUBLE_KW" ]

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
    RULE_valueList = 10
    RULE_funcCall = 11

    ruleNames =  [ "program", "funcdef", "signature", "inputArgs", "expression", 
                   "expressionList", "returnStmt", "typedValue", "assignment", 
                   "typedValueList", "valueList", "funcCall" ]

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
    SCALAR=12
    NAME=13
    INTEGER=14
    Newline=15
    Whitespace=16
    ALPHANUMERIC=17
    SIGN=18
    VAR_TYPE=19
    VOID_KW=20
    INT_KW=21
    DOUBLE_KW=22

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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.funcdef()
                self.state = 27 
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
            self.state = 29
            self.signature()
            self.state = 30
            self.match(MambaParser.T__0)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7 or _la==MambaParser.NAME:
                self.state = 31
                self.expression()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
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
            self.state = 39
            self.match(MambaParser.T__2)
            self.state = 40
            self.match(MambaParser.NAME)
            self.state = 41
            self.inputArgs()
            self.state = 42
            self.match(MambaParser.T__3)
            self.state = 43
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
            self.state = 45
            self.match(MambaParser.T__4)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME:
                self.state = 46
                self.typedValueList()


            self.state = 49
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 51
                self.assignment()
                pass

            elif la_ == 2:
                self.state = 52
                self.returnStmt()
                pass

            elif la_ == 3:
                self.state = 53
                self.funcCall()
                pass

            elif la_ == 4:
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 54
                    self.match(MambaParser.NAME)
                    self.state = 57 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MambaParser.NAME):
                        break

                pass


            self.state = 61
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
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7 or _la==MambaParser.NAME:
                self.state = 63
                self.expression()
                self.state = 68
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

        def funcCall(self):
            return self.getTypedRuleContext(MambaParser.FuncCallContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MambaParser.T__7)
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 70
                self.match(MambaParser.NAME)

            elif la_ == 2:
                self.state = 71
                self.match(MambaParser.INTEGER)

            elif la_ == 3:
                self.state = 72
                self.funcCall()


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
            self.state = 75
            self.match(MambaParser.NAME)
            self.state = 76
            self.match(MambaParser.T__8)
            self.state = 77
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
            self.state = 79
            self.match(MambaParser.NAME)
            self.state = 80
            self.match(MambaParser.T__9)
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(MambaParser.INTEGER)
                pass

            elif la_ == 2:
                self.state = 82
                self.match(MambaParser.NAME)
                pass

            elif la_ == 3:
                self.state = 83
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
            self.state = 86
            self.typedValue()
            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__10:
                self.state = 87
                self.match(MambaParser.T__10)
                self.state = 88
                self.typedValue()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCALAR(self, i:int=None):
            if i is None:
                return self.getTokens(MambaParser.SCALAR)
            else:
                return self.getToken(MambaParser.SCALAR, i)

        def getRuleIndex(self):
            return MambaParser.RULE_valueList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueList" ):
                listener.enterValueList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueList" ):
                listener.exitValueList(self)




    def valueList(self):

        localctx = MambaParser.ValueListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_valueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(MambaParser.SCALAR)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__10:
                self.state = 95
                self.match(MambaParser.T__10)
                self.state = 96
                self.match(MambaParser.SCALAR)
                self.state = 101
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

        def valueList(self):
            return self.getTypedRuleContext(MambaParser.ValueListContext,0)


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
        self.enterRule(localctx, 22, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(MambaParser.NAME)
            self.state = 103
            self.match(MambaParser.T__4)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.SCALAR:
                self.state = 104
                self.valueList()


            self.state = 107
            self.match(MambaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





