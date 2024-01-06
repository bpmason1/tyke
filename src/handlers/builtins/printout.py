from ..base import BaseHandler
from llvmlite import ir
from builder.ProgramNode import ProgramNode
from utils import fail_fast

class __PrintoutHandler(BaseHandler):
    __printCnt = 0

    def handle_printlnFuncCall(self, callCtx, builder, newScopeObj):
        self.handle_printfFuncCall(callCtx, builder, newScopeObj, True)

    def handle_printFuncCall(self, callCtx, builder, newScopeObj):
        self.handle_printfFuncCall(callCtx, builder, newScopeObj, False)

    def handle_printfFuncCall(self, callCtx, builder, newScopeObj, appendNewLine):
        int8 = ir.IntType(8)
        int32 = ir.IntType(32)

        package = ProgramNode.getPackage('main')

        dataListCtx = callCtx.funcCallDataList().dataList()
        dataList = dataListCtx.data()
        assert(len(dataList) == 1) #  TODO - allow printf varargs

        dataCtx = dataList[0]
        printf_args = []

        lineTerminated = '\n\0' if appendNewLine else '\0'
        if dataCtx.expression() and dataCtx.expression().simpleExpression():
            simpExprCtx = dataCtx.expression().simpleExpression()
            if simpExprCtx.NAME():
                varName = simpExprCtx.NAME().getText()
                varArg = newScopeObj.read(varName, builder)
                printf_args.append(varArg)
                # text = str(newScopeObj.read(varName, builder)) + '\n\0'
                text = '%d' + lineTerminated
                text = text.encode('utf_8')
            elif simpExprCtx.primitive():
                primitiveCtx = simpExprCtx.primitive()
                if primitiveCtx.STRING():
                    text = str(primitiveCtx.STRING())[1:-1] + lineTerminated
                    text = text.encode('utf_8')
                elif primitiveCtx.numeric():
                    numericCtx = primitiveCtx.numeric()
                    text = self.handle_numeric(numericCtx, builder, newScopeObj).get_reference() + lineTerminated
                    text = text.encode('utf_8')
                else:
                    fail_fast('WTF - printout')
        else:
            fail_fast(f'failed print-statment for text "{dataCtx.getText()}"')

        # text = dataList[0].encode('utf_8')

        size = len(text) + 1

        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(text)),
                                bytearray(text))

        arrayType = ir.ArrayType(int8, len(text))
        glbl = ir.GlobalVariable(package.llvmIR(), arrayType, f"print_call_{self.__printCnt}")
        self.__printCnt += 1
        glbl.initializer = c_fmt

        const = [ir.Constant(int32, x) for x in [0, 0]]
        elemPtr = builder.gep(glbl, const, inbounds=True, name='d')
        callFn = package.getFunction('printf').llvmIR()

        result = builder.call(callFn, [elemPtr] + printf_args)
        # return result

PrintoutHandler = __PrintoutHandler()
