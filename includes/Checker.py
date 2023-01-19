from includes.Process import *
from includes.Initialize import _COLOR_ACCEPT, _COLOR_CE, _COLOR_RE, _COLOR_TLE, _COLOR_WRONG, _NAME_OF_OUTPUT, _NAME_OF_ANSWER, _STYLE_BRIGHT, _STYLE_RESET_ALL, _USER_DIRECTORY, _DEFAULT_CHECKER
from includes.Initialize import _DEFAULT_MESSAGE_ACCEPT, _RETURN_CODE_ACCEPT
from includes.Initialize import _DEFAULT_MESSAGE_WRONG, _RETURN_CODE_WRONG
from includes.Initialize import _DEFAULT_MESSAGE_RE, _RETURN_CODE_RE
from includes.Initialize import _DEFAULT_MESSAGE_TLE, _RETURN_CODE_TLE
from includes.Initialize import _DEFAULT_MESSAGE_CE, _RETURN_CODE_CE

class Checker (Process) :
    def __init__(self, filePath: str) -> None:
        self.isDefaultChecker = (filePath == _DEFAULT_CHECKER)
        if (not self.isDefaultChecker) :
            super().__init__(filePath)
        
    def run(self, stdInput: str = None, argv: list = []):
        """
            Parameters:
                - stdInput (str) : standar input (Default = None)
                - argv (list) : list of argument (Default = [])
                
            Return :
                - [message || _DEFAULT_MESSAGE_ACCEPT, _RETURN_CODE_ACCEPT] = Accept testcase
                - [message || _DEFAULT_MESSAGE_WRONG, _RETURN_CODE_WRONG] = Wrong testcase
                - [_DEFAULT_MESSAGE_TLE, _RETURN_CODE_TLE] = Checker timelimit exceeded
                - [_DEFAULT_MESSAGE_RE, _RETURN_CODE_RE] = Checker runtime error
                - [_DEFAULT_MESSAGE_CE, _RETURN_CODE_CE] = Checker compiled error
        """
        if (self.isDefaultChecker) :
            fout = open(_USER_DIRECTORY + "/" + _NAME_OF_OUTPUT, "r")
            fans = open(_USER_DIRECTORY + "/" + _NAME_OF_ANSWER, "r")
            
            if (fout.read().strip() == fans.read().strip()) :
                return [_STYLE_BRIGHT + _COLOR_ACCEPT + _DEFAULT_MESSAGE_ACCEPT + _STYLE_RESET_ALL, _RETURN_CODE_ACCEPT]
            else :
                return [_STYLE_BRIGHT + _COLOR_WRONG + _DEFAULT_MESSAGE_WRONG + _STYLE_RESET_ALL, _RETURN_CODE_WRONG]
        else :
            returnCode = super().run(
                stdInput=stdInput, 
                argv=[_USER_DIRECTORY + "/" + _NAME_OF_OUTPUT, _USER_DIRECTORY + "/" + _NAME_OF_ANSWER] + argv
            )
            
            if (returnCode == _RETURN_CODE_TLE) :
                return [_STYLE_BRIGHT + _COLOR_TLE + _DEFAULT_MESSAGE_TLE + _STYLE_RESET_ALL, _RETURN_CODE_TLE]
            if (returnCode == _RETURN_CODE_RE) :
                return [_STYLE_BRIGHT + _COLOR_RE + _DEFAULT_MESSAGE_RE + _STYLE_RESET_ALL, _RETURN_CODE_RE]
            if (returnCode == _RETURN_CODE_CE) :
                return [_STYLE_BRIGHT + _COLOR_CE + _DEFAULT_MESSAGE_CE + _STYLE_RESET_ALL, _RETURN_CODE_CE]
            return [self.stdout(), self.returncode()]
            