from llvmlite import ir

from .AstNode import AstNode
from .FunctionNode import FunctionNode

class PackageNode(AstNode):
    def __init__(self, name: str, parent: AstNode):
        super().__init__(name, parent=parent)
        self.__llvm = ir.Module(name= name)

    # funcArgs: TypedValue
    def newFunction(self, name: str, returnType, funcArgs):
        return FunctionNode(name, returnType, funcArgs, parent=self)

    def getFunction(self, name):
        for node in self.children:
            if node.name == name:
                return node
        return None

    def llvmIR(self):
        return self.__llvm
