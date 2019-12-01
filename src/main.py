from antlr4 import *
from colorama import Fore, Style
from llvmlite import ir
from MambaLexer import MambaLexer
from MambaListener import MambaListener
from MambaParser import MambaParser
import re
import sys

from function_table import FunctionTable
from handlers import ExpressionHandler

module = ir.Module(name='__file__')  # create better name

def string_to_ir_type(str_type: str):
    if str_type == 'void':
        return ir.VoidType()
    elif str_type == 'int':
        return ir.IntType(64)
    elif str_type == 'double':
        return ir.DoubleType()
    print(Fore.RED + f'ERROR: string_to_ir_type unknown type {str_type}' + Style.RESET_ALL)
    return 'Unknown'

def get_ir_func(name, returnType, inputTypeList):
    global module

    fnty = ir.FunctionType(returnType, inputTypeList)  # ingore input types for now
    return ir.Function(module, fnty, name=name)

class MambaFunctionTableBuilder(MambaListener):
    def enterFuncdef(self, ctx):
        '''
        Create an LLVM IR function based on `ctx.signature()`
        '''
        sigCtx = ctx.signature()
        name = sigCtx.NAME().getText()
        returnType = string_to_ir_type( sigCtx.getChild(-1).getText() )
        inputArgs = sigCtx.inputArgs()
        inputTypedValueList = inputArgs.typedValueList()

        inputTypes = []
        argNames = []
        if hasattr(inputTypedValueList, 'typedValue'):
            for tv in inputTypedValueList.typedValue():
                argType = string_to_ir_type(tv.getChild(-1).getText())
                # print( str(argType) )
                inputTypes.append(argType)
                argNames.append( tv.NAME() )

        irFunc = get_ir_func(name, returnType, inputTypes)
        FunctionTable.setFunction(name, irFunc, argNames)

class MambaPrintListener(MambaListener):
    def exitFuncdef(self, ctx):
        # print( f'Exiting {id(ctx)}' )
        pass

    def enterFuncdef(self, ctx):
        # symbolTable = {}

        sigCtx = ctx.signature()
        name = sigCtx.NAME().getText()
        irFunc = FunctionTable.getFunction(name)

        # a, b = irFunc.args
        block = irFunc.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        result = irFunc.return_value.type(0) # this is a junk default value
        exprList = ctx.expression()
        for exprCtx in exprList:
            ExpressionHandler.handle(exprCtx, builder)
            if exprCtx.returnStmt():
                callCtx = exprCtx.returnStmt()
                tmpRes = callCtx.getChild(-1).getText()
                if re.match('\d', tmpRes):

                    # **************************************
                    result = irFunc.return_value.type(tmpRes)
                    # **************************************

                elif len(tmpRes) > 2 and tmpRes[-2:] == '()':
                    callName = tmpRes[:-2]
                    callFn = FunctionTable.getFunction(callName)
                    i64 = ir.IntType(64)
                    result = builder.call(callFn, [ i64(3) ])


        builder.ret(result)
        # for idx in range( ctx.getChildCount() ):
        #     print( ctx.getChild(idx).getText() )
        # print( "\n" )


def main():
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

    print(module)

if __name__ == '__main__':
    main()
