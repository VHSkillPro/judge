import argparse
from includes.Initialize import _DEFAULT_CHECKER, _NUMBER_OF_TEST

class Argument :
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
    
    def get_argument(self) -> list :
        self.parser.add_argument("-code", "--code", dest="code", help="File need judge")
        self.parser.add_argument("-sol", "--sol", dest="sol", help="File solution")
        self.parser.add_argument("-gen", "--gen", dest="gen", help="File generation testcase")
        self.parser.add_argument("-nt", "--nTest", dest="nTest", default=_NUMBER_OF_TEST, help="Number of testcase",type=int)
        self.parser.add_argument("-ck", "--checker", dest="checker", default=_DEFAULT_CHECKER, help="File checker")
        
        args = self.parser.parse_args()
        return [args.code, args.sol, args.gen, args.nTest, args.checker]