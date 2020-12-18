from llvmlite import ir

from .AstNode import AstNode
from .DeclarationNode import DeclarationNode
from .FunctionNode import FunctionNode
# from collections import OrderedDict
from colorama import Fore, Style
import sys

class PackageNode(AstNode):
    def __init__(self, name: str, parent: AstNode):
        super().__init__(name, parent=parent)
        self.__llvm = ir.Module(name=name)
        self.__types = {}

    # funcArgs: TypedValue
    def newFunction(self, name: str, returnType, funcArgs):
        return FunctionNode(name, returnType, funcArgs, parent=self)

    def newDeclaration(self, name: str, returnType, funcArgs):
        return DeclarationNode(name, returnType, funcArgs, parent=self, hasVarArg=True)

    def getTypeInfo(self, name):
        return self.__types[name]

    def newVariableType(self, name, ordElemDict, llvmType):
        if name in self.__types:
            msg = f'Error - type {name} already declared\n'
            sys.stderr.write(msg)
            sys.exit(5)
        self.__types[name] = (ordElemDict, llvmType)

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
