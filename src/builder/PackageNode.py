from llvmlite import ir

from .AstNode import AstNode
from .DeclarationNode import DeclarationNode
from .FunctionNode import FunctionNode
from colorama import Fore, Style
import sys

class PackageNode(AstNode):
    def __init__(self, name: str, parent: AstNode):
        super().__init__(name, parent=parent)
        self.__llvm = ir.Module(name=name)

    # funcArgs: TypedValue
    def newFunction(self, name: str, returnType, funcArgs):
        return FunctionNode(name, returnType, funcArgs, parent=self)

    def newDeclaration(self, name: str, returnType, funcArgs):
        return DeclarationNode(name, returnType, funcArgs, parent=self, hasVarArg=True)

    def getFunction(self, name):
        for node in self.children:
            if node.name == name:
                return node
        sys.stderr.write(Fore.RED + f'Undefined function "{name}"' + Style.RESET_ALL + '\n')
        sys.exit(1)

    def llvmIR(self):
        return self.__llvm

    def __str__(self):
        llvm = ''
        for line in str(self.__llvm).splitlines():
            if not line.startswith('target '):
                llvm += (line + '\n')
        return llvm
