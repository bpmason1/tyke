import sys

_RED = '\x1b[31m'
_RESET_ALL = '\x1b[0m'

def fail_fast(msg, exit_code=66):
    sys.stderr.write(_RED + msg + _RESET_ALL + '\n')
    sys.exit(exit_code)
