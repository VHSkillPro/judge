from colorama import *

# Checker
_DEFAULT_CHECKER = "diff"

# Path of user
_USER_DIRECTORY = "user"

# Timelimit (Can customize)
_DEFAULT_TIME_LIMIT = 1000 # ms

# Number of test (Can customize)
_NUMBER_OF_TEST = 100

# File contain data inp, out, ans
_NAME_OF_OUTPUT = "data.out"
_NAME_OF_INPUT = "data.inp"
_NAME_OF_ANSWER = "data.ans"

# RETURN CODE
_RETURN_CODE_ACCEPT = 0
_RETURN_CODE_WRONG = 1
_RETURN_CODE_TLE = 2
_RETURN_CODE_RE = 3
_RETURN_CODE_CE = 4

# MESSAGE (Can customize)
_DEFAULT_MESSAGE_ACCEPT = Fore.GREEN + "AC !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_WRONG = Fore.RED + "WA !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_TLE = Fore.RED + "TLE !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_RE = Fore.YELLOW + "RE !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_CE = Fore.MAGENTA + "Compile error !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_CHECKER_TLE = Fore.RED + "Checker timelimit exceeded !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_CHECKER_RE = Fore.YELLOW + "Checker runtime error !!" + Style.RESET_ALL
_DEFAULT_MESSAGE_CHECKER_CE = Fore.MAGENTA + "Checker compiled error !!" + Style.RESET_ALL