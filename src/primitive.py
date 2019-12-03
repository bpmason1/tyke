from colorama import Fore, Style
from llvmlite import ir
from keywords import *

class __Primitive:
    def __init__(self):
        self._void = ir.VoidType()
        self._integer = ir.IntType(64)
        self._double = ir.DoubleType()
        self._type_map = {
            VOID: self._void,
            INT: self._integer,
            DOUBLE: self._double
        }

    def get_type_by_name(self, var_type: str):
        if var_type in self._type_map:
            return self._type_map[var_type]

        msg = f'ERROR: Primitive.get_type_by_name unknown type {var_type}'
        print(Fore.RED + msg + Style.RESET_ALL)
        return 'Unknown'

    @property
    def int(self):
        return self._type_map[INT]

    @property
    def double(self):
        return self._type_map[DOUBLE]

    @property
    def void(self):
        return self._type_map[VOID]

Primitive = __Primitive()
