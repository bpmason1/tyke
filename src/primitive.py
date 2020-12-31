from colorama import Fore, Style
from llvmlite import ir
from keywords import *

class __Primitive:
    def __init__(self):
        self._type_map = {
            VOID: ir.VoidType(),
            INT: ir.IntType(64),
            DOUBLE: ir.DoubleType(),
            BOOL: ir.IntType(1),
        }

    def get_type_by_name(self, var_type: str):
        if var_type in self._type_map:
            return self._type_map[var_type]

        msg = f'ERROR: Primitive.get_type_by_name unknown type {var_type}'
        print(Fore.RED + msg + Style.RESET_ALL)
        return None

    def get_name_by_type(self, var_type):
        for name, typeObj in self._type_map.items():
            if isinstance(var_type, type(typeObj)):
                return name
        return None

    @property
    def boolean(self):
        return self._type_map[BOOL]

    @property
    def integer(self):
        return self._type_map[INT]

    @property
    def double(self):
        return self._type_map[DOUBLE]

    @property
    def void(self):
        return self._type_map[VOID]

Primitive = __Primitive()
