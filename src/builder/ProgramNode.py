from .AstNode import AstNode
from .PackageNode import PackageNode

class __ProgramNode(AstNode):
    def __init__(self):
        super().__init__('tyke')
        std = self.newPackage('std')

    def llvmIR(self):
        None

    def newPackage(self, name: str) -> PackageNode:
        if self.getPackage(name):
            raise Exception(f'ERROR: Package {name} already exists')

        return PackageNode(name, parent=self)

    def getPackage(self, name: str) -> PackageNode:
        for node in self.children:
            if node.name == name:
                return node
        return None

ProgramNode = __ProgramNode()
