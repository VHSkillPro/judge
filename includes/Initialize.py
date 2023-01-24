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
_DEFAULT_MESSAGE_ACCEPT = "AC !!"
_DEFAULT_MESSAGE_WRONG = "WA !!"
_DEFAULT_MESSAGE_TLE = "TLE !!"
_DEFAULT_MESSAGE_RE = "RE !!"
_DEFAULT_MESSAGE_CE = "Compile error !!"
_DEFAULT_MESSAGE_CHECKER_TLE = "Checker timelimit exceeded !!"
_DEFAULT_MESSAGE_CHECKER_RE = "Checker runtime error !!"
_DEFAULT_MESSAGE_CHECKER_CE = "Checker compiled error !!"

# COLOR (Can customize)
_COLOR_ACCEPT = Fore.GREEN
_COLOR_WRONG = Fore.RED
_COLOR_TLE = Fore.RED
_COLOR_RE = Fore.YELLOW
_COLOR_CE = Fore.MAGENTA

# STYLE 
_STYLE_RESET_ALL = Style.RESET_ALL
_STYLE_BRIGHT = Style.BRIGHT