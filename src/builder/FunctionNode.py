from llvmlite import ir

from .AstNode import AstNode

class FunctionNode(AstNode):
    def __init__(self, name: str, returnType, funcArgs, parent):
        super().__init__(name, parent=parent)

        argTypes = [a.type for a in funcArgs]
        fnty = ir.FunctionType(returnType, argTypes)  # ingore input types for now
        self.__llvm = ir.Function(parent.llvmIR(), fnty, name=name)
        self.__funcArgs = funcArgs
        self.__blocks = {}
        self.__newBlock("entry")


    def llvmIR(self):
        return self.__llvm

    def getBlock(self, name):
        return self.__blocks[name]

    def __newBlock(self, name):
        if name not in self.__blocks:
            irFunc = self.llvmIR()
            block = irFunc.append_basic_block(name=name)
            self.__blocks[name] = block
        return self.__blocks[name]

    @property
    def args(self):
        return self.__funcArgs
