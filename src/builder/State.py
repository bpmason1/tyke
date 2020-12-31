from collections import OrderedDict
from colorama import Fore, Style
from contextlib import contextmanager
from enum import Enum
from llvmlite import ir
from llvmlite.ir.instructions import LoadInstr
from llvmlite.ir.values import Constant
import sys
from primitive import Primitive
from utils import fail_fast

class Mutability(Enum):
    UNDEFINED = 0
    MUTABLE = 1
    IMMUTABLE = 2

class StackPtr:
    def __init__(self, name, valType):
        self._name = name
        self._valType = valType

    def write(self, name, builder):
        builder.store(self.valType, value)   # generates the LLVM to store value on the stack

class Scope:
    def __init__(self):
        # self.__args = {}
        self._mutable = {}
        self._immutable = {}

class State:
    def __init__(self):
        self._scopes = [Scope()]
        self._uninitialized = set()

    def _add_scope(self):
        newScope = Scope()
        self._scopes.append(newScope)
        # self.print_num_scopes()

    def _del_scope(self):
        if self._scopes:
            self._scopes.pop()
        else:
            sys.stderr.write('ERROR: no scopes remaining to pop\n')
            sys.exit(1)
        # self.print_num_scopes()

    def getStackPtr(self, name):
        scopeIdx = self.num_scopes - 1
        while scopeIdx >= 0:
            if name in self._scopes[scopeIdx]._immutable:
                return (self._scopes[scopeIdx]._immutable[name], Mutability.IMMUTABLE)

            if name in self._scopes[scopeIdx]._mutable:
                return (self._scopes[scopeIdx]._mutable[name], Mutability.MUTABLE)

            scopeIdx -= 1
        return (None, Mutability.UNDEFINED)

    def allocate(self, name, builder, varType, size=1, mutable=False):
        if not isinstance(name, str):
            fail_fast("Name must be of type 'str'", 1)

        if self.getStackPtr(name)[0]:
            msg = f'ERROR: attempting to shadow variable {name}'
            fail_fast(msg, 1)

        builder.position_at_start(builder.block)
        scope = self._scopes[-1]
        stackPtr = builder.alloca(varType, size=size, name=name)
        if mutable:
            scope._mutable[name] = stackPtr
        else:
            scope._immutable[name] = stackPtr
        builder.position_at_end(builder.block)

        self._uninitialized.add(name)
        return stackPtr

    def get_type(self, name):
        stackPtr, _ = self.getStackPtr(name)
        return stackPtr.type.pointee

    def _getStructFieldPtr(self, fieldNameList: list, builder, package):
        int32 = ir.IntType(32)
        zero = int32(0)

        if len(fieldNameList) <= 1:
            sys.stderr.write(f'Undefined call to State.read_struct with only {len(fieldNameList)} names in fieldNameList\n')
            sys.exit(1)

        stackPtr, _ = self.getStackPtr(fieldNameList[0])
        pointee = stackPtr.type.pointee

        indices = [zero ]  # [start_idx, field_idx]
        for fieldName in fieldNameList[1:]:
            typeName = pointee.name
            ordElemDict, _ = package.getTypeInfo(typeName)
            for idx, (fieldNameFound, fieldTypeFound) in enumerate(ordElemDict.items()):
                if fieldName == fieldNameFound:
                    indices.append(int32(idx))
                    typeName = pointee.elements[idx]
                    pointee = pointee.elements[idx]
                    break
        elemPtr = builder.gep(stackPtr, indices, inbounds=True)  # TODO: what the heck does the inbounds field do???
        return elemPtr

    def read_struct(self, fieldNameList: list, builder, package):
        elemPtr = self._getStructFieldPtr(fieldNameList, builder, package)
        return builder.load(elemPtr)

    def read(self, name, builder):
        stackPtr, _ = self.getStackPtr(name)

        if not stackPtr:
            msg = f'ERROR: no such variable {name}'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

        return builder.load(stackPtr)

    def initialize_struct(self, name: str, structData, ordFieldDict: OrderedDict, builder):
        stackPtr, mutability = self.getStackPtr(name)
        if name in self._uninitialized:
            self._uninitialized.remove(name)
        elif mutability == Mutability.IMMUTABLE:
            msg = f'ERROR: trying to modify immutable struct variable "{name}"\n'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

        self._write_internal_struct(stackPtr, structData, builder)

    def _write_internal_struct(self, stackPtr, structData, builder):
        int32 = ir.IntType(32)
        zero = int32(0)

        for idx, fieldCtx in enumerate(structData.constant):
            indices = [zero, int32(idx)]  # [start_idx, field_idx]
            elemPtr = builder.gep(stackPtr, indices, inbounds=True)  # TODO: what the heck does the inbounds field do???

            if isinstance(fieldCtx, LoadInstr):
                builder.store(fieldCtx, elemPtr)
            elif isinstance(fieldCtx, Constant) and isinstance(fieldCtx.type, type(Primitive.integer)):
                builder.store(fieldCtx, elemPtr)
            else:
                self._write_internal_struct(elemPtr, fieldCtx, builder)
                # for eIdx, elemCtx in enumerate(fieldCtx.constant):
                #     indices = [zero, int32(idx), int32(eIdx)]
                #     elemPtr = builder.gep(stackPtr, indices, inbounds=True)  # TODO: what the heck does the inbounds field do???
                #     builder.store(elemCtx, elemPtr)

    def write_struct(self, fieldNameList: list, value, builder, package):
        elemPtr = self._getStructFieldPtr(fieldNameList, builder, package)
        builder.store(value, elemPtr)

    def write(self, name, value, builder):
        stackPtr, mutability = self.getStackPtr(name)
        if not stackPtr:
            msg = f'Error: Variable "{name}" has not been declared\n'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

        # the variable has alredy been allocated on the stack
        if name in self._uninitialized:
            builder.store(value, stackPtr)
            self._uninitialized.remove(name)
            return
        elif mutability == Mutability.IMMUTABLE:
            # the variable has been initialized ... is it mutable???
                msg = f'ERROR: trying to modify immutable variable "{name}"\n'
                sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
                sys.exit(1)

        builder.store(value, stackPtr)   # generates the LLVM to store value on the stack

    @property
    def num_scopes(self):
        return len(self._scopes)

    def print_num_scopes(self):
        sys.stderr.write(f'Scopes: {len(self._scopes)}')

@contextmanager
def new_scope(state):
    state._add_scope()
    try:
        yield state
    finally:
        state._del_scope
