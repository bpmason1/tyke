# Generated from Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\3\3")
        buf.write("\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\5\5,\n\5\3\5\3\5\3\6\3\6\6\6\62\n\6")
        buf.write("\r\6\16\6\63\5\6\66\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\t\7\tC\n\t\f\t\16\tF\13\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2H\2\25\3\2\2\2\4")
        buf.write("\31\3\2\2\2\6#\3\2\2\2\b)\3\2\2\2\n\65\3\2\2\2\f9\3\2")
        buf.write("\2\2\16=\3\2\2\2\20?\3\2\2\2\22G\3\2\2\2\24\26\5\4\3\2")
        buf.write("\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2")
        buf.write("\2\30\3\3\2\2\2\31\32\5\6\4\2\32\36\7\3\2\2\33\35\5\n")
        buf.write("\6\2\34\33\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2")
        buf.write("\2\2\37!\3\2\2\2 \36\3\2\2\2!\"\7\4\2\2\"\5\3\2\2\2#$")
        buf.write("\7\5\2\2$%\7\f\2\2%&\5\b\5\2&\'\7\6\2\2\'(\7\22\2\2(\7")
        buf.write("\3\2\2\2)+\7\7\2\2*,\5\20\t\2+*\3\2\2\2+,\3\2\2\2,-\3")
        buf.write("\2\2\2-.\7\b\2\2.\t\3\2\2\2/\66\5\22\n\2\60\62\7\f\2\2")
        buf.write("\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2\2")
        buf.write("\2\64\66\3\2\2\2\65/\3\2\2\2\65\61\3\2\2\2\66\67\3\2\2")
        buf.write("\2\678\7\t\2\28\13\3\2\2\29:\7\f\2\2:;\7\n\2\2;<\7\22")
        buf.write("\2\2<\r\3\2\2\2=>\5\n\6\2>\17\3\2\2\2?D\5\f\7\2@A\7\13")
        buf.write("\2\2AC\5\f\7\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2")
        buf.write("E\21\3\2\2\2FD\3\2\2\2GH\7\f\2\2HI\7\7\2\2IJ\7\b\2\2J")
        buf.write("\23\3\2\2\2\b\27\36+\63\65D")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'def'", "'->'", "'('", 
                     "')'", "';'", "':'", "','", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'void'", "'int'", "'double'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NAME", "INTEGER", "Newline", 
                      "Whitespace", "ALPHANUMERIC", "SIGN", "VAR_TYPE", 
                      "VOID_KW", "INT_KW", "DOUBLE_KW" ]

    RULE_program = 0
    RULE_funcdef = 1
    RULE_signature = 2
    RULE_inputArgs = 3
    RULE_expression = 4
    RULE_typedValue = 5
    RULE_main = 6
    RULE_typedValueList = 7
    RULE_funcCall = 8

    ruleNames =  [ "program", "funcdef", "signature", "inputArgs", "expression", 
                   "typedValue", "main", "typedValueList", "funcCall" ]

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
    NAME=10
    INTEGER=11
    Newline=12
    Whitespace=13
    ALPHANUMERIC=14
    SIGN=15
    VAR_TYPE=16
    VOID_KW=17
    INT_KW=18
    DOUBLE_KW=19

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.funcdef()
                self.state = 21 
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
            self.state = 23
            self.signature()
            self.state = 24
            self.match(MambaParser.T__0)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.NAME:
                self.state = 25
                self.expression()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 31
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
            self.state = 33
            self.match(MambaParser.T__2)
            self.state = 34
            self.match(MambaParser.NAME)
            self.state = 35
            self.inputArgs()
            self.state = 36
            self.match(MambaParser.T__3)
            self.state = 37
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
            self.state = 39
            self.match(MambaParser.T__4)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME:
                self.state = 40
                self.typedValueList()


            self.state = 43
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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 45
                self.funcCall()
                pass

            elif la_ == 2:
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 46
                    self.match(MambaParser.NAME)
                    self.state = 49 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MambaParser.NAME):
                        break

                pass


            self.state = 53
            self.match(MambaParser.T__6)
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
        self.enterRule(localctx, 10, self.RULE_typedValue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(MambaParser.NAME)
            self.state = 56
            self.match(MambaParser.T__7)
            self.state = 57
            self.match(MambaParser.VAR_TYPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MambaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = MambaParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.expression()
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
        self.enterRule(localctx, 14, self.RULE_typedValueList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.typedValue()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__8:
                self.state = 62
                self.match(MambaParser.T__8)
                self.state = 63
                self.typedValue()
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
        self.enterRule(localctx, 16, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self.match(MambaParser.NAME)
            self.state = 70
            self.match(MambaParser.T__4)
            self.state = 71
            self.match(MambaParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





