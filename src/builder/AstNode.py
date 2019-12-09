from abc import ABC, abstractmethod
from anytree import Node

class AstNode(ABC, Node):
    def __init__(self, name, parent=None):
        super().__init__(name, parent=parent)

    @abstractmethod
    def llvmIR(self):
        raise NotImplementedError('uninmplement method llvmIR')
