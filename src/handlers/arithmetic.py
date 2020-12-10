from MambaParser import MambaParser
import sys


def get_operator(opCtx: MambaParser.Arithmetic_opContext):
    op = None
    if opCtx.ADD():
        op = opCtx.ADD()
    elif opCtx.SUBTRACT():
        op = opCtx.SUBTRACT()
    elif opCtx.MULTIPLY():
        op = opCtx.MULTIPLY()
    elif opCtx.DIVIDE():
        op = opCtx.DIVIDE()

    if not op:
        sys.stderr.write("No valid arithmetic operator found")
        sys.exit(2)

    return op.getText()
    