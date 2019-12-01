# Generated from Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("*\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\6\3\23\n\3\r\3\16\3\24\3\4\3\4\3\4")
        buf.write("\6\4\32\n\4\r\4\16\4\33\3\5\3\5\3\5\5\5!\n\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2(\2\r\3\2")
        buf.write("\2\2\4\22\3\2\2\2\6\31\3\2\2\2\b\35\3\2\2\2\n$\3\2\2\2")
        buf.write("\f\16\5\b\5\2\r\f\3\2\2\2\16\17\3\2\2\2\17\r\3\2\2\2\17")
        buf.write("\20\3\2\2\2\20\3\3\2\2\2\21\23\7\7\2\2\22\21\3\2\2\2\23")
        buf.write("\24\3\2\2\2\24\22\3\2\2\2\24\25\3\2\2\2\25\5\3\2\2\2\26")
        buf.write("\27\5\4\3\2\27\30\7\3\2\2\30\32\3\2\2\2\31\26\3\2\2\2")
        buf.write("\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\7\3\2\2")
        buf.write("\2\35\36\5\n\6\2\36 \7\4\2\2\37!\5\6\4\2 \37\3\2\2\2 ")
        buf.write("!\3\2\2\2!\"\3\2\2\2\"#\7\5\2\2#\t\3\2\2\2$%\7\t\2\2%")
        buf.write("&\7\r\2\2&\'\7\6\2\2\'(\7\16\2\2(\13\3\2\2\2\6\17\24\33")
        buf.write(" ")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'{'", "'}'", "'->'", "<INVALID>", 
                     "<INVALID>", "'def'", "'double'", "'int'", "'void'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'0'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ALPHANUMERIC", "INTEGER", "KW_DEF", 
                      "KW_DOUBLE", "KW_INT", "KW_VOID", "NAME", "RETURN_TYPE", 
                      "VAR_TYPE", "ZERO", "Newline", "Whitespace" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_expressionList = 2
    RULE_funcdef = 3
    RULE_signature = 4

    ruleNames =  [ "program", "expression", "expressionList", "funcdef", 
                   "signature" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    ALPHANUMERIC=5
    INTEGER=6
    KW_DEF=7
    KW_DOUBLE=8
    KW_INT=9
    KW_VOID=10
    NAME=11
    RETURN_TYPE=12
    VAR_TYPE=13
    ZERO=14
    Newline=15
    Whitespace=16

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
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.funcdef()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.KW_DEF):
                    break

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

        def ALPHANUMERIC(self, i:int=None):
            if i is None:
                return self.getTokens(MambaParser.ALPHANUMERIC)
            else:
                return self.getToken(MambaParser.ALPHANUMERIC, i)

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
        self.enterRule(localctx, 2, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.match(MambaParser.ALPHANUMERIC)
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.ALPHANUMERIC):
                    break

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
        self.enterRule(localctx, 4, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.expression()
                self.state = 21
                self.match(MambaParser.T__0)
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.ALPHANUMERIC):
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


        def expressionList(self):
            return self.getTypedRuleContext(MambaParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 6, self.RULE_funcdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.signature()
            self.state = 28
            self.match(MambaParser.T__1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.ALPHANUMERIC:
                self.state = 29
                self.expressionList()


            self.state = 32
            self.match(MambaParser.T__2)
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

        def KW_DEF(self):
            return self.getToken(MambaParser.KW_DEF, 0)

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def RETURN_TYPE(self):
            return self.getToken(MambaParser.RETURN_TYPE, 0)

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
        self.enterRule(localctx, 8, self.RULE_signature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MambaParser.KW_DEF)
            self.state = 35
            self.match(MambaParser.NAME)
            self.state = 36
            self.match(MambaParser.T__3)
            self.state = 37
            self.match(MambaParser.RETURN_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





