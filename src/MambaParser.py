# Generated from Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("[\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3\3\3\5\3\'")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\6\5\62\n\5\r")
        buf.write("\5\16\5\63\3\6\3\6\3\7\3\7\3\7\5\7;\n\7\3\7\3\7\3\b\3")
        buf.write("\b\5\bA\n\b\3\b\3\b\3\t\3\t\3\t\7\tH\n\t\f\t\16\tK\13")
        buf.write("\t\3\n\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16")
        buf.write("\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\2\4\3\2\f\16\3\2\f\r\2S\2\37\3\2\2\2\4#\3\2\2\2\6")
        buf.write("*\3\2\2\2\b\61\3\2\2\2\n\65\3\2\2\2\f\67\3\2\2\2\16>\3")
        buf.write("\2\2\2\20D\3\2\2\2\22L\3\2\2\2\24P\3\2\2\2\26R\3\2\2\2")
        buf.write("\30T\3\2\2\2\32V\3\2\2\2\34X\3\2\2\2\36 \5\4\3\2\37\36")
        buf.write("\3\2\2\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\3\3\2\2\2")
        buf.write("#$\5\6\4\2$&\7\3\2\2%\'\5\b\5\2&%\3\2\2\2&\'\3\2\2\2\'")
        buf.write("(\3\2\2\2()\7\4\2\2)\5\3\2\2\2*+\7\5\2\2+,\7\23\2\2,-")
        buf.write("\5\16\b\2-.\7\6\2\2./\5\32\16\2/\7\3\2\2\2\60\62\5\n\6")
        buf.write("\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3\2\2\2\63\64\3\2")
        buf.write("\2\2\64\t\3\2\2\2\65\66\5\f\7\2\66\13\3\2\2\2\67:\7\7")
        buf.write("\2\28;\5\26\f\29;\5\24\13\2:8\3\2\2\2:9\3\2\2\2:;\3\2")
        buf.write("\2\2;<\3\2\2\2<=\7\17\2\2=\r\3\2\2\2>@\7\b\2\2?A\5\20")
        buf.write("\t\2@?\3\2\2\2@A\3\2\2\2AB\3\2\2\2BC\7\t\2\2C\17\3\2\2")
        buf.write("\2DI\5\22\n\2EF\7\n\2\2FH\5\22\n\2GE\3\2\2\2HK\3\2\2\2")
        buf.write("IG\3\2\2\2IJ\3\2\2\2J\21\3\2\2\2KI\3\2\2\2LM\7\23\2\2")
        buf.write("MN\7\13\2\2NO\5\34\17\2O\23\3\2\2\2PQ\7\20\2\2Q\25\3\2")
        buf.write("\2\2RS\7\21\2\2S\27\3\2\2\2TU\7\23\2\2U\31\3\2\2\2VW\t")
        buf.write("\2\2\2W\33\3\2\2\2XY\t\3\2\2Y\35\3\2\2\2\b!&\63:@I")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'def'", "'->'", "'return'", 
                     "'('", "')'", "','", "':'", "'double'", "'int'", "'void'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "KW_DOUBLE", "KW_INT", "KW_VOID", 
                      "SEMICOLON", "DOUBLE", "INTEGER", "RETURN_TYPE", "NAME", 
                      "Newline", "Whitespace" ]

    RULE_program = 0
    RULE_funcdef = 1
    RULE_signature = 2
    RULE_statementList = 3
    RULE_statement = 4
    RULE_returnStmt = 5
    RULE_funcDefArgList = 6
    RULE_typedArgList = 7
    RULE_typedArg = 8
    RULE_double = 9
    RULE_integer = 10
    RULE_name = 11
    RULE_returnType = 12
    RULE_varType = 13

    ruleNames =  [ "program", "funcdef", "signature", "statementList", "statement", 
                   "returnStmt", "funcDefArgList", "typedArgList", "typedArg", 
                   "double", "integer", "name", "returnType", "varType" ]

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
    KW_DOUBLE=10
    KW_INT=11
    KW_VOID=12
    SEMICOLON=13
    DOUBLE=14
    INTEGER=15
    RETURN_TYPE=16
    NAME=17
    Newline=18
    Whitespace=19

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.funcdef()
                self.state = 31 
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


        def statementList(self):
            return self.getTypedRuleContext(MambaParser.StatementListContext,0)


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
            self.state = 33
            self.signature()
            self.state = 34
            self.match(MambaParser.T__0)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.T__4:
                self.state = 35
                self.statementList()


            self.state = 38
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

        def funcDefArgList(self):
            return self.getTypedRuleContext(MambaParser.FuncDefArgListContext,0)


        def returnType(self):
            return self.getTypedRuleContext(MambaParser.ReturnTypeContext,0)


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
            self.state = 40
            self.match(MambaParser.T__2)
            self.state = 41
            self.match(MambaParser.NAME)
            self.state = 42
            self.funcDefArgList()
            self.state = 43
            self.match(MambaParser.T__3)
            self.state = 44
            self.returnType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.StatementContext)
            else:
                return self.getTypedRuleContext(MambaParser.StatementContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)




    def statementList(self):

        localctx = MambaParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statementList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 46
                self.statement()
                self.state = 49 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.T__4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStmt(self):
            return self.getTypedRuleContext(MambaParser.ReturnStmtContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = MambaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.returnStmt()
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

        def SEMICOLON(self):
            return self.getToken(MambaParser.SEMICOLON, 0)

        def integer(self):
            return self.getTypedRuleContext(MambaParser.IntegerContext,0)


        def double(self):
            return self.getTypedRuleContext(MambaParser.DoubleContext,0)


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
        self.enterRule(localctx, 10, self.RULE_returnStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(MambaParser.T__4)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MambaParser.INTEGER]:
                self.state = 54
                self.integer()
                pass
            elif token in [MambaParser.DOUBLE]:
                self.state = 55
                self.double()
                pass
            elif token in [MambaParser.SEMICOLON]:
                pass
            else:
                pass
            self.state = 58
            self.match(MambaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedArgList(self):
            return self.getTypedRuleContext(MambaParser.TypedArgListContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_funcDefArgList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDefArgList" ):
                listener.enterFuncDefArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDefArgList" ):
                listener.exitFuncDefArgList(self)




    def funcDefArgList(self):

        localctx = MambaParser.FuncDefArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDefArgList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(MambaParser.T__5)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME:
                self.state = 61
                self.typedArgList()


            self.state = 64
            self.match(MambaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedArgListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typedArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.TypedArgContext)
            else:
                return self.getTypedRuleContext(MambaParser.TypedArgContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_typedArgList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedArgList" ):
                listener.enterTypedArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedArgList" ):
                listener.exitTypedArgList(self)




    def typedArgList(self):

        localctx = MambaParser.TypedArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typedArgList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.typedArg()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7:
                self.state = 67
                self.match(MambaParser.T__7)
                self.state = 68
                self.typedArg()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedArgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def varType(self):
            return self.getTypedRuleContext(MambaParser.VarTypeContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_typedArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedArg" ):
                listener.enterTypedArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedArg" ):
                listener.exitTypedArg(self)




    def typedArg(self):

        localctx = MambaParser.TypedArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typedArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(MambaParser.NAME)
            self.state = 75
            self.match(MambaParser.T__8)
            self.state = 76
            self.varType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLE(self):
            return self.getToken(MambaParser.DOUBLE, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_double

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDouble" ):
                listener.enterDouble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDouble" ):
                listener.exitDouble(self)




    def double(self):

        localctx = MambaParser.DoubleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_double)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MambaParser.DOUBLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(MambaParser.INTEGER, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = MambaParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(MambaParser.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = MambaParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(MambaParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VOID(self):
            return self.getToken(MambaParser.KW_VOID, 0)

        def KW_INT(self):
            return self.getToken(MambaParser.KW_INT, 0)

        def KW_DOUBLE(self):
            return self.getToken(MambaParser.KW_DOUBLE, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_returnType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnType" ):
                listener.enterReturnType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnType" ):
                listener.exitReturnType(self)




    def returnType(self):

        localctx = MambaParser.ReturnTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MambaParser.KW_DOUBLE) | (1 << MambaParser.KW_INT) | (1 << MambaParser.KW_VOID))) != 0)):
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


    class VarTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DOUBLE(self):
            return self.getToken(MambaParser.KW_DOUBLE, 0)

        def KW_INT(self):
            return self.getToken(MambaParser.KW_INT, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_varType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarType" ):
                listener.enterVarType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarType" ):
                listener.exitVarType(self)




    def varType(self):

        localctx = MambaParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(_la==MambaParser.KW_DOUBLE or _la==MambaParser.KW_INT):
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





