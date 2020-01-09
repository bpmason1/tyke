from llvmlite import ir

from .AstNode import AstNode

class DeclarationNode(AstNode):
    def __init__(self, name: str, returnType, argTypes, parent=None, hasVarArg=False):
        super().__init__(name, parent=parent)

        fnty = ir.FunctionType(returnType, argTypes, var_arg=hasVarArg)
        self.__llvm = ir.Function(parent.llvmIR(), fnty, name=name)

    def llvmIR(self):
        return self.__llvm
