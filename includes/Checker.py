from includes.Process import *
from includes.Initialize import _NAME_OF_OUTPUT, _NAME_OF_ANSWER, _USER_DIRECTORY, _DEFAULT_CHECKER, _DEFAULT_MESSAGE_ACCEPT, _DEFAULT_MESSAGE_WRONG

class Checker (Process) :
    def __init__(self, filePath: str) -> None:
        self.isDefaultChecker = (filePath == _DEFAULT_CHECKER)
        if (filePath != _DEFAULT_CHECKER) :
            super().__init__(filePath)
        
    def run(self, stdInput: str = None, argv: list = []):
        if (self.isDefaultChecker) :
            fout = open(_USER_DIRECTORY + "/" + _NAME_OF_OUTPUT, "r")
            fans = open(_USER_DIRECTORY + "/" + _NAME_OF_ANSWER, "r")
            
            if (fout.read().strip() == fans.read().strip()) :
                return [_DEFAULT_MESSAGE_ACCEPT, 0]
            else :
                return [_DEFAULT_MESSAGE_WRONG, 1]
        else :
            process = super().run(
                stdInput=stdInput, 
                argv=[_USER_DIRECTORY + "/" + _NAME_OF_OUTPUT, _USER_DIRECTORY + "/" + _NAME_OF_ANSWER] + argv,
                isCheck=False
            )
            return [process.stdout.decode("utf-8"), process.returncode]