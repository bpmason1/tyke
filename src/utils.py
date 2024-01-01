from colorama import Fore, Style
import sys

def warn(msg):
    print(Fore.YELLOW + Style.BRIGHT + msg + Style.RESET_ALL)

def fail_fast(msg, exit_code=66):
    sys.stderr.write(Fore.RED + msg + Style.RESET_ALL + '\n')
    sys.exit(exit_code)
