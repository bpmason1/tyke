# Generated from Mamba.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\6\2$\n\2\r\2\16")
        buf.write("\2%\3\3\3\3\3\3\5\3+\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\5\6\5\66\n\5\r\5\16\5\67\3\6\3\6\5\6<\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\5\7C\n\7\3\7\3\7\3\b\3\b\3\b\3\t\3\t\5\t")
        buf.write("L\n\t\3\t\3\t\3\n\3\n\3\n\7\nS\n\n\f\n\16\nV\13\n\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\5\ra\n\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\7\16h\n\16\f\16\16\16k\13\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \2\5\4\2\20\21\23\23\3\2\r\17\3\2\r\16")
        buf.write("\2n\2#\3\2\2\2\4\'\3\2\2\2\6.\3\2\2\2\b\65\3\2\2\2\n;")
        buf.write("\3\2\2\2\f=\3\2\2\2\16F\3\2\2\2\20I\3\2\2\2\22O\3\2\2")
        buf.write("\2\24W\3\2\2\2\26[\3\2\2\2\30^\3\2\2\2\32d\3\2\2\2\34")
        buf.write("l\3\2\2\2\36n\3\2\2\2 p\3\2\2\2\"$\5\4\3\2#\"\3\2\2\2")
        buf.write("$%\3\2\2\2%#\3\2\2\2%&\3\2\2\2&\3\3\2\2\2\'(\5\6\4\2(")
        buf.write("*\7\3\2\2)+\5\b\5\2*)\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\7")
        buf.write("\4\2\2-\5\3\2\2\2./\7\5\2\2/\60\7\23\2\2\60\61\5\20\t")
        buf.write("\2\61\62\7\6\2\2\62\63\5\36\20\2\63\7\3\2\2\2\64\66\5")
        buf.write("\n\6\2\65\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3")
        buf.write("\2\2\28\t\3\2\2\29<\5\f\7\2:<\5\16\b\2;9\3\2\2\2;:\3\2")
        buf.write("\2\2<\13\3\2\2\2=B\7\7\2\2>C\7\21\2\2?C\7\20\2\2@C\5\26")
        buf.write("\f\2AC\7\23\2\2B>\3\2\2\2B?\3\2\2\2B@\3\2\2\2BA\3\2\2")
        buf.write("\2BC\3\2\2\2CD\3\2\2\2DE\7\f\2\2E\r\3\2\2\2FG\5\26\f\2")
        buf.write("GH\7\f\2\2H\17\3\2\2\2IK\7\b\2\2JL\5\22\n\2KJ\3\2\2\2")
        buf.write("KL\3\2\2\2LM\3\2\2\2MN\7\t\2\2N\21\3\2\2\2OT\5\24\13\2")
        buf.write("PQ\7\n\2\2QS\5\24\13\2RP\3\2\2\2SV\3\2\2\2TR\3\2\2\2T")
        buf.write("U\3\2\2\2U\23\3\2\2\2VT\3\2\2\2WX\7\23\2\2XY\7\13\2\2")
        buf.write("YZ\5 \21\2Z\25\3\2\2\2[\\\7\23\2\2\\]\5\30\r\2]\27\3\2")
        buf.write("\2\2^`\7\b\2\2_a\5\32\16\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2")
        buf.write("\2bc\7\t\2\2c\31\3\2\2\2di\5\34\17\2ef\7\n\2\2fh\5\34")
        buf.write("\17\2ge\3\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\33\3\2")
        buf.write("\2\2ki\3\2\2\2lm\t\2\2\2m\35\3\2\2\2no\t\3\2\2o\37\3\2")
        buf.write("\2\2pq\t\4\2\2q!\3\2\2\2\13%*\67;BKT`i")
        return buf.getvalue()


class MambaParser ( Parser ):

    grammarFileName = "Mamba.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'{'", "'}'", "'def'", "'->'", "'return'", 
                     "'('", "')'", "','", "':'", "';'", "'double'", "'int'", 
                     "'void'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SEMICOLON", "KW_DOUBLE", 
                      "KW_INT", "VOID", "DOUBLE", "INTEGER", "RETURN_TYPE", 
                      "NAME", "Newline", "Whitespace" ]

    RULE_program = 0
    RULE_funcdef = 1
    RULE_signature = 2
    RULE_statementList = 3
    RULE_statement = 4
    RULE_returnStmt = 5
    RULE_funcCallStmt = 6
    RULE_funcDefArgList = 7
    RULE_typedArgList = 8
    RULE_typedArg = 9
    RULE_funcCall = 10
    RULE_funcCallDataList = 11
    RULE_dataList = 12
    RULE_data = 13
    RULE_returnType = 14
    RULE_varType = 15

    ruleNames =  [ "program", "funcdef", "signature", "statementList", "statement", 
                   "returnStmt", "funcCallStmt", "funcDefArgList", "typedArgList", 
                   "typedArg", "funcCall", "funcCallDataList", "dataList", 
                   "data", "returnType", "varType" ]

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
    SEMICOLON=10
    KW_DOUBLE=11
    KW_INT=12
    VOID=13
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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.funcdef()
                self.state = 35 
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
            self.state = 37
            self.signature()
            self.state = 38
            self.match(MambaParser.T__0)
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.T__4 or _la==MambaParser.NAME:
                self.state = 39
                self.statementList()


            self.state = 42
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
            self.state = 44
            self.match(MambaParser.T__2)
            self.state = 45
            self.match(MambaParser.NAME)
            self.state = 46
            self.funcDefArgList()
            self.state = 47
            self.match(MambaParser.T__3)
            self.state = 48
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
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.statement()
                self.state = 53 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MambaParser.T__4 or _la==MambaParser.NAME):
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


        def funcCallStmt(self):
            return self.getTypedRuleContext(MambaParser.FuncCallStmtContext,0)


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
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MambaParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.returnStmt()
                pass
            elif token in [MambaParser.NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self.funcCallStmt()
                pass
            else:
                raise NoViableAltException(self)

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

        def INTEGER(self):
            return self.getToken(MambaParser.INTEGER, 0)

        def DOUBLE(self):
            return self.getToken(MambaParser.DOUBLE, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MambaParser.FuncCallContext,0)


        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

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
            self.state = 59
            self.match(MambaParser.T__4)
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 60
                self.match(MambaParser.INTEGER)

            elif la_ == 2:
                self.state = 61
                self.match(MambaParser.DOUBLE)

            elif la_ == 3:
                self.state = 62
                self.funcCall()

            elif la_ == 4:
                self.state = 63
                self.match(MambaParser.NAME)


            self.state = 66
            self.match(MambaParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(MambaParser.FuncCallContext,0)


        def SEMICOLON(self):
            return self.getToken(MambaParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_funcCallStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallStmt" ):
                listener.enterFuncCallStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallStmt" ):
                listener.exitFuncCallStmt(self)




    def funcCallStmt(self):

        localctx = MambaParser.FuncCallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcCallStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.funcCall()
            self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_funcDefArgList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(MambaParser.T__5)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MambaParser.NAME:
                self.state = 72
                self.typedArgList()


            self.state = 75
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
        self.enterRule(localctx, 16, self.RULE_typedArgList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.typedArg()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7:
                self.state = 78
                self.match(MambaParser.T__7)
                self.state = 79
                self.typedArg()
                self.state = 84
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
        self.enterRule(localctx, 18, self.RULE_typedArg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MambaParser.NAME)
            self.state = 86
            self.match(MambaParser.T__8)
            self.state = 87
            self.varType()
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

        def funcCallDataList(self):
            return self.getTypedRuleContext(MambaParser.FuncCallDataListContext,0)


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
            self.state = 89
            self.match(MambaParser.NAME)
            self.state = 90
            self.funcCallDataList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallDataListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataList(self):
            return self.getTypedRuleContext(MambaParser.DataListContext,0)


        def getRuleIndex(self):
            return MambaParser.RULE_funcCallDataList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallDataList" ):
                listener.enterFuncCallDataList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallDataList" ):
                listener.exitFuncCallDataList(self)




    def funcCallDataList(self):

        localctx = MambaParser.FuncCallDataListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcCallDataList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(MambaParser.T__5)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MambaParser.DOUBLE) | (1 << MambaParser.INTEGER) | (1 << MambaParser.NAME))) != 0):
                self.state = 93
                self.dataList()


            self.state = 96
            self.match(MambaParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MambaParser.DataContext)
            else:
                return self.getTypedRuleContext(MambaParser.DataContext,i)


        def getRuleIndex(self):
            return MambaParser.RULE_dataList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataList" ):
                listener.enterDataList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataList" ):
                listener.exitDataList(self)




    def dataList(self):

        localctx = MambaParser.DataListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dataList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.data()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MambaParser.T__7:
                self.state = 99
                self.match(MambaParser.T__7)
                self.state = 100
                self.data()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(MambaParser.NAME, 0)

        def DOUBLE(self):
            return self.getToken(MambaParser.DOUBLE, 0)

        def INTEGER(self):
            return self.getToken(MambaParser.INTEGER, 0)

        def getRuleIndex(self):
            return MambaParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)




    def data(self):

        localctx = MambaParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MambaParser.DOUBLE) | (1 << MambaParser.INTEGER) | (1 << MambaParser.NAME))) != 0)):
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


    class ReturnTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOID(self):
            return self.getToken(MambaParser.VOID, 0)

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
        self.enterRule(localctx, 28, self.RULE_returnType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MambaParser.KW_DOUBLE) | (1 << MambaParser.KW_INT) | (1 << MambaParser.VOID))) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
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





