from includes.Process import *
from includes.Initialize import _NAME_OF_OUTPUT, _NAME_OF_ANSWER, _DEFAULT_CHECKER, _USER_DIRECTORY

class Checker (Process) :
    def __init__(self, filePath: str = _DEFAULT_CHECKER) -> None:
        super().__init__(filePath)
        
    def run(self, stdInput: str = None, argv: list = []):
        return super().run(
            stdInput=stdInput, 
            argv=[_USER_DIRECTORY + "/" + _NAME_OF_OUTPUT, _USER_DIRECTORY + "/" + _NAME_OF_ANSWER] + argv, 
            isCheck=False
        )