from antlr4 import *
from colorama import Fore, Style
from llvmlite import ir
from MambaLexer import MambaLexer
from MambaListener import MambaListener
from MambaParser import MambaParser
import re
import sys

from typed_value import TypedValue
from handlers import ExpressionHandler
from primitive import Primitive

from builder.ProgramNode import ProgramNode

package = ProgramNode.newPackage('main')


def builtinFunctions():
    main = ProgramNode.getPackage('main')

    void = Primitive.void
    i8_ptr = ir.PointerType(ir.IntType(8))
    main.newDeclaration("printf", ir.IntType(32), tuple([i8_ptr]))
    # declare i32 @printf(i8*, ...)

    # funcNode = package.newFunction("print", returnType, argList)
    return

class MambaFunctionTableBuilder(MambaListener):
    def enterFuncdef(self, ctx):
        '''
        Create an LLVM IR function based on `ctx.signature()`
        '''
        package = ProgramNode.getPackage('main')

        sigCtx = ctx.signature()
        name = sigCtx.NAME().getText()
        returnType = Primitive.get_type_by_name( sigCtx.returnType().getText() )
        typedArgList = sigCtx.funcDefArgList().typedArgList()
        # inputTypedValueList = inputArgs.typedValueList()

        argList = []
        argNames = []

        # if the function has args
        if hasattr(typedArgList, 'typedArg'):
            for tv in typedArgList.typedArg():
                # print( tv.NAME().getSymbol().text )
                argName = tv.NAME().getText()
                argType = Primitive.get_type_by_name(tv.varType().getText())
                arg = TypedValue(argName, argType)
                argList.append( arg )

        argValues = [a.type for a in argList]

        # funcNode = package.newFunction(name, returnType, argList)
        package.newFunction(name, returnType, argList)

class MambaPrintListener(MambaListener):
    def exitFuncdef(self, ctx):
        # print( f'Exiting {id(ctx)}' )
        pass

    def enterFuncdef(self, ctx):
        package = ProgramNode.getPackage('main')

        sigCtx = ctx.signature()
        name = sigCtx.NAME().getText()
        fnAst = package.getFunction(name)

        funcArgs = fnAst.args

        block = fnAst.getBlock("entry")
        builder = ir.IRBuilder(block)

        stmtList = ctx.statementList()

        state = {}
        irFunc = fnAst.llvmIR()
        for idx in range(len(irFunc.args)):
            argName = funcArgs[idx].value
            argType = funcArgs[idx].type

            builder.position_at_start(block)
            state[argName] = builder.alloca(argType, name=argName)
            builder.position_at_end(block)

            # print( dir(irFunc.args[idx]) )
            builder.store(irFunc.args[idx], state[argName])

        if stmtList:
            for exprCtx in stmtList.statement():
                if exprCtx.funcCallStmt():
                    sys.stderr.write("........... Function Call Statement")
                    stmtCtx = exprCtx.funcCallStmt()
                    ExpressionHandler.handle_funcCall(stmtCtx.funcCall(), builder)

                elif exprCtx.returnStmt():
                    sys.stderr.write("........... Return Statement")
                    retStmt = exprCtx.returnStmt()
                    ExpressionHandler.handle_returnStmt(retStmt, builder, irFunc, state)

                elif exprCtx.assigmentStmt():
                    sys.stderr.write("........... Assignment Statement")
                    assignCtx = exprCtx.assigmentStmt()
                    ExpressionHandler.handle_assigmentStmt(assignCtx, builder, irFunc, state)

                else:
                    sys.stderr.write("........... WTF ?!?")


def main():
    # these exist regardless of the program being compiled
    builtinFunctions()

    # lexer = MambaLexer(StdinStream())
    lexer = MambaLexer(FileStream('hello.mamba'))
    stream = CommonTokenStream(lexer)
    parser = MambaParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()

    fnBuilder = MambaFunctionTableBuilder()
    walker.walk(fnBuilder, tree)

    printer = MambaPrintListener()
    walker.walk(printer, tree)

    print(ProgramNode.getPackage('std'))
    print(ProgramNode.getPackage('main'))

if __name__ == '__main__':
    main()
