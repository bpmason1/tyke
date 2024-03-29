from TykeParser import TykeParser
from llvmlite.ir.types import DoubleType, IntType
import sys


def get_llvmlite_arithmetic_function(valType, opCtx: TykeParser.Arithmetic_opContext, builder):
    if isinstance(valType, IntType):
        return get_integer_operator(opCtx, builder)
    elif isinstance(valType, DoubleType):
        return get_double_operator(opCtx, builder)
    else:
        sys.stderr.write(f'Unknown numeric type: {str(valType)}')
        sys.exit(2)

def get_double_operator(opCtx: TykeParser.Arithmetic_opContext, builder):
    if opCtx.ADD():
        return builder.fadd
    elif opCtx.SUBTRACT():
        return builder.fsub
    elif opCtx.MULTIPLY():
        return builder.fmul
    elif opCtx.DIVIDE():
        return builder.fdiv
    else:
        sys.stderr.write(f'Unknown integer operator: {opCtx.getText()}')
        sys.exit(2)

def get_integer_operator(opCtx: TykeParser.Arithmetic_opContext, builder):
    if hasattr(opCtx, 'ADD') and opCtx.ADD():
        return builder.add
    elif hasattr(opCtx, 'SUBTRACT') and opCtx.SUBTRACT():
        return builder.sub
    elif hasattr(opCtx, 'MULTIPLY') and opCtx.MULTIPLY():
        return builder.mul
    elif hasattr(opCtx, 'DIVIDE') and opCtx.DIVIDE():
        return builder.sdiv
    else:
        sys.stderr.write(f'Unknown integer operator: {opCtx.getText()}')
        sys.exit(2)

def get_comparison_operator(opCtx, builder):
    if opCtx.EQ():
        return '=='
    elif opCtx.NEQ():
        return '!='
    elif opCtx.GT():
        return '>'
    elif opCtx.GTE():
        return '>='
    elif opCtx.LT():
        return '<'
    elif opCtx.LTE():
        return '<='

    sys.stderr.write(f'Unknwon numerical comparison operator {opCtx.getText()}')
    sys.exit(2)
