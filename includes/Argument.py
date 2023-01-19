import argparse
from includes.Initialize import _DEFAULT_CHECKER, _NUMBER_OF_TEST, _DEFAULT_TIME_LIMIT

class Argument :
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
    
    def get_argument(self) -> list :
        """
            Return : [code, sol, gen, nTest, checker, timelimit]
                - code : File need judge
                - sol : File solution
                - gen : File generation testcase
                - nTest : Number of testcase
                - checker : File checker
                - timelimit : Time limit of file need judge
        """
        self.parser.add_argument("-code", "--code", dest="code", help="File need judge")
        self.parser.add_argument("-sol", "--sol", dest="sol", help="File solution")
        self.parser.add_argument("-gen", "--gen", dest="gen", help="File generation testcase")
        self.parser.add_argument("-nt", "--nTest", dest="nTest", default=_NUMBER_OF_TEST, help="Number of testcase",type=int)
        self.parser.add_argument("-ck", "--checker", dest="checker", default=_DEFAULT_CHECKER, help="File checker")
        self.parser.add_argument("-tl", "--timelimit", dest="timelimit", default=_DEFAULT_TIME_LIMIT, help="Time limit of file need judge", type=int)
        
        args = self.parser.parse_args()
        return [args.code, args.sol, args.gen, args.nTest, args.checker, args.timelimit / 1000]