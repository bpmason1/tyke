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
from builder.State import State, new_scope

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
        This is to ensure function calls are defined before attempting to call them.
        It allows functions to be written in any order in the source file.
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

        state = State()
        irFunc = fnAst.llvmIR()
        
        for idx in range(len(irFunc.args)):
            argName = funcArgs[idx].value
            argType = funcArgs[idx].type

            # allocate space on the stack at the top of the function
            state.allocate(argName, builder, argType, mutable=False)

            # store the value on the stack after all stack space has been allocated
            state.write(argName, irFunc.args[idx], builder)

        if stmtList:
            for exprCtx in stmtList.statement():
                if exprCtx.funcCallStmt():
                    # sys.stderr.write("........... Function Call Statement")
                    stmtCtx = exprCtx.funcCallStmt()
                    ExpressionHandler.handle_funcCall(stmtCtx.funcCall(), builder, state)

                elif exprCtx.returnStmt():
                    # sys.stderr.write("........... Return Statement")
                    retStmt = exprCtx.returnStmt()
                    ExpressionHandler.handle_returnStmt(retStmt, builder, irFunc, state)

                elif exprCtx.declareAndAssignStmt():
                    declAndAssign = exprCtx.declareAndAssignStmt()
                    ExpressionHandler.handle_declareAndAssignStmt(declAndAssign, builder, irFunc, state)
                elif exprCtx.assigmentStmt():
                    # sys.stderr.write("........... Assignment Statement")
                    assignCtx = exprCtx.assigmentStmt()
                    ExpressionHandler.handle_assigmentStmt(assignCtx, builder, irFunc, state)
                elif exprCtx.conditionalStmt():
                    conditionalCtx = exprCtx.conditionalStmt()
                    ExpressionHandler.handle_conditionalStmt(conditionalCtx, builder, irFunc, state)
                    # ifCtx = conditionalCtx.ifStmt()
                    # ExpressionHandler.handle_ifStmt(ifCtx, builder, irFunc, state)
                else:
                    sys.stderr.write("........... WTF ?!?\n")
                    sys.exit(1)

def processCodeStr(srcCode: str):
    # these exist regardless of the program being compiled


    # lexer = MambaLexer(FileStream('hello.mamba'))
    lexer = MambaLexer(InputStream(srcCode))
    stream = CommonTokenStream(lexer)
    parser = MambaParser(stream)
    tree = parser.program()
    walker = ParseTreeWalker()

    fnBuilder = MambaFunctionTableBuilder()
    walker.walk(fnBuilder, tree)

    printer = MambaPrintListener()
    walker.walk(printer, tree)

    # print(ProgramNode.getPackage('std'))
    return {'main': ProgramNode.getPackage('main')}

def processCodeFile(filename):
    builtinFunctions()

    with open(filename, 'r') as fd:
        pacakgeMapLL = processCodeStr(fd.read())

    print(pacakgeMapLL['main'])

if __name__ == '__main__':
    processCodeFile('./hello.mamba')
