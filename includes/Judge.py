import sys
from includes.Process import *
from includes.Checker import *
from includes.Generator import *
from includes.Initialize import _NUMBER_OF_TEST, _DEFAULT_CHECKER

class Judge :
    def __init__(self) -> None:
        self.codeFile = sys.argv[1]
        self.solFile = sys.argv[2]
        self.genFile = sys.argv[3]
        self.nTest = _NUMBER_OF_TEST if len(sys.argv) < 5 else sys.argv[4]
        self.checkerFile = _DEFAULT_CHECKER if len(sys.argv) < 6 else sys.argv[5]
        pass
    
    def run(self) :
        pass