from llvmlite import ir

from .AstNode import AstNode

class FunctionNode(AstNode):
    def __init__(self, name: str, returnType, funcArgs, parent):
        super().__init__(name, parent=parent)

        argTypes = [a.type for a in funcArgs]
        fnty = ir.FunctionType(returnType, argTypes)  # ingore input types for now
        self.__llvm = ir.Function(parent.llvmIR(), fnty, name=name)
        self.__funcArgs = funcArgs

    def llvmIR(self):
        return self.__llvm

    @property
    def args(self):
        return self.__funcArgs
