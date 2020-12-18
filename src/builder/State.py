from colorama import Fore, Style
from contextlib import contextmanager
from enum import Enum
import sys

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

    def has(self, name):
        scopeIdx = self.num_scopes - 1
        while scopeIdx >= 0:
            if name in self._scopes[scopeIdx]._immutable:
                return (True, Mutability.IMMUTABLE)

            if name in self._scopes[scopeIdx]._mutable:
                return (True, Mutability.MUTABLE)

            scopeIdx -= 1
        return (False, Mutability.UNDEFINED)

    def allocate(self, name, builder, varType, size=1, mutable=False):
        if not isinstance(name, str):
            msg = "Name must be of type 'str'\n"
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

        if self.has(name)[0]:
            msg = f'ERROR: attempting to shadow variable {name}'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

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

    def read(self, name, builder):
        scopeIdx = self.num_scopes - 1
        while scopeIdx >= 0:
            if name in self._scopes[scopeIdx]._immutable:
                stackPtr = self._scopes[scopeIdx]._immutable[name]
                return builder.load(stackPtr)

            if name in self._scopes[scopeIdx]._mutable:
                stackPtr = self._scopes[scopeIdx]._mutable[name]
                return builder.load(stackPtr)

            scopeIdx -= 1

        msg = f'ERROR: no such variable {name}'
        sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
        sys.exit(1)

    def write(self, name, value, builder):
        exists, mutability = self.has(name)
        if not exists:
            msg = f'Error: Variable "{name}" has not been declared\n'
            sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
            sys.exit(1)

        # the variable has alredy been allocated on the stack
        if name in self._uninitialized:
            self._write_uninitialized(name, value, builder)
            return
        elif mutability == Mutability.IMMUTABLE:
            # the variable has been initialized ... is it mutable???
                msg = f'ERROR: trying to modify immutable variable "{name}"\n'
                sys.stderr.write(Fore.RED + msg + Style.RESET_ALL)
                sys.exit(1)

        self._write_mutable( name, value, builder)

    def _write_mutable(self, name, value, builder):
        # update the variable ... assumes the variable has already been allocated on the stack
        scopeIdx = self.num_scopes - 1
        while scopeIdx >= 0:
            if name in self._scopes[scopeIdx]._mutable:
                stackPtr = self._scopes[scopeIdx]._mutable[name]
                builder.store(value, stackPtr)   # generates the LLVM to store value on the stack
                return
            scopeIdx -= 1

    def _write_uninitialized(self, name, value, builder):
        stackPtr = None
        scopeIdx = self.num_scopes - 1
        while scopeIdx >= 0:
            if name in self._scopes[scopeIdx]._immutable:
                # check immutable varibales
                stackPtr = self._scopes[scopeIdx]._immutable[name]
            elif name in self._scopes[scopeIdx]._mutable:
                # check mutable varibales
                stackPtr = self._scopes[scopeIdx]._mutable[name]

            if stackPtr:
                builder.store(value, stackPtr)   # generates the LLVM to store value on the stack
                # stackPtr = value   # update the stack data within this compiler State object

                # remove `name` from set of uninitialized variables
                self._uninitialized.remove(name)
                return

            # `name` not found in this scope ... check the next scope
            scopeIdx -= 1

        sys.stderr.write(f'Could not find uninitialize variable {name}')
        sys.exit(1)

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
