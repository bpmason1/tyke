from antlr4 import *
from collections import OrderedDict
from llvmlite import ir
from TykeLexer import TykeLexer
from TykeListener import TykeListener
from TykeParser import TykeParser
import os
import sys

from typed_value import TypedValue
from handlers import ExpressionHandler
from primitive import Primitive
from utils import fail_fast, warn

from builder.ProgramNode import ProgramNode
from builder.FunctionNode import FunctionNode
from builder.State import State

package = ProgramNode.newPackage('main')


def builtinFunctions():
    main = ProgramNode.getPackage('main')

    void = Primitive.void
    i8_ptr = ir.PointerType(ir.IntType(8))
    main.newDeclaration("printf", ir.IntType(32), tuple([i8_ptr]))
    # declare i32 @printf(i8*, ...)

    # funcNode = package.newFunction("print", returnType, argList)
    return

class TykeTypedefBuilder(TykeListener):
    def enterTypedef(self, ctx):
        main = ProgramNode.getPackage('main')

        typeName = ctx.NAME().getText()
        if ctx.typedArgList():
            typedArgList = ctx.typedArgList().typedArg()
            structFieldTypeList = []
            structFieldDict = OrderedDict()
            for typedArg in typedArgList:
                varTypeName = typedArg.varType().getText()
                llvmVarType = main.get_type_by_name(varTypeName)
                name = typedArg.NAME().getText()
                structFieldTypeList.append(llvmVarType)
                structFieldDict[name] = llvmVarType
        moduleCtx = main.llvmIR().context
        identType = moduleCtx.get_identified_type(name=typeName)
        identType.set_body(*structFieldTypeList)
        # print(identType.get_declaration())

        package.newVariableType(typeName, structFieldDict, identType)
        # sys.stderr.write("INFO - Exiting TykeTypedefBuilder\n")

class TykeFunctionTableBuilder(TykeListener):
    def enterFuncdef(self, ctx):
        '''
        Create an LLVM IR function based on `ctx.signature()`
        This is to ensure function calls are defined before attempting to call them.
        It allows functions to be written in any order in the source file.
        '''
        package = ProgramNode.getPackage('main')

        sigCtx = ctx.signature()
        name = sigCtx.NAME().getText()
        returnType = package.get_type_by_name( sigCtx.returnType().getText() )
        typedArgList = sigCtx.funcDefArgList().typedArgList()
        # inputTypedValueList = inputArgs.typedValueList()

        argList = []

        # if the function has args
        if hasattr(typedArgList, 'typedArg'):
            for tv in typedArgList.typedArg():
                # print( tv.NAME().getSymbol().text )
                argName = tv.NAME().getText()
                argType = package.get_type_by_name(tv.varType().getText())
                arg = TypedValue(argName, argType)
                argList.append(arg)

        # funcNode = package.newFunction(name, returnType, argList)
        package.newFunction(name, returnType, argList)

class TykePrintListener(TykeListener):
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
        irFunc: FunctionNode = fnAst.llvmIR()
        
        for idx in range(len(irFunc.args)):
            argName = funcArgs[idx].value
            argType = funcArgs[idx].type

            # allocate space on the stack at the top of the function
            state.allocate(argName, builder, argType, mutable=False)

            # store the value on the stack after all stack space has been allocated
            state.write(argName, irFunc.args[idx], builder)

        if stmtList:
            ExpressionHandler.handle_statementList(stmtList, builder, irFunc, state)

def processCode(parsedFileDict):
    for walker, tree in parsedFileDict.values():
        typeBuilder = TykeTypedefBuilder()
        walker.walk(typeBuilder, tree)

    for walker, tree in parsedFileDict.values():
        fnBuilder = TykeFunctionTableBuilder()
        walker.walk(fnBuilder, tree)

    for walker, tree in parsedFileDict.values():
        printer = TykePrintListener()
        walker.walk(printer, tree)

    # print(ProgramNode.getPackage('std'))
    return {'main': ProgramNode.getPackage('main')}

def parseFile(filename):
    with open(filename, 'r') as fd:
        srcCode = fd.read()
        lexer = TykeLexer(InputStream(srcCode))
        stream = CommonTokenStream(lexer)
        parser = TykeParser(stream)
        tree = parser.program()
        walker = ParseTreeWalker()
        return (walker, tree)

def run(all_file_list):
    # these exist regardless of the program being compiled
    builtinFunctions()

    parsedFileDict = {}
    for filename in all_file_list:
        parsedFileDict[filename] = parseFile(filename)

    return processCode(parsedFileDict)

if __name__ == '__main__':
    currDir = os.path.dirname(__file__)

    if len(sys.argv) != 2:
      fail_fast("ERROR - first (and only argument) should be the directory with tyke source code")
      sys.exit(1)
    appDir = sys.argv[1]
    #appDir = path.join(currDir, '..', 'example', 'src')

    all_file_list = [os.path.join(appDir, f) for f in os.listdir(appDir) if f.endswith('.ty')]

    if len(all_file_list) < 1:
        fail_fast('ERROR - program must have at least 1 file')
    else:
        pacakgeMapLL = run(all_file_list)
        print(pacakgeMapLL['main'])

