from includes.Process import *
from includes.Checker import *
from includes.Generator import *
from includes.Argument import *
from includes.Cleaner import *
from includes.Initialize import _USER_DIRECTORY, _NAME_OF_INPUT, _NAME_OF_OUTPUT, _NAME_OF_ANSWER
from includes.Initialize import _DEFAULT_MESSAGE_ACCEPT, _RETURN_CODE_ACCEPT
from includes.Initialize import _DEFAULT_MESSAGE_WRONG, _RETURN_CODE_WRONG
from includes.Initialize import _DEFAULT_MESSAGE_CE, _RETURN_CODE_CE
from includes.Initialize import _DEFAULT_MESSAGE_TLE, _RETURN_CODE_TLE
from includes.Initialize import _DEFAULT_MESSAGE_RE, _RETURN_CODE_RE

class Judge :
    def __init__(self) -> None:
        argv = Argument().get_argument()

        self.codeProcess = Process(argv[0])
        self.solProcess = Process(argv[1])
        self.generator = Generator(argv[2])
        self.nTest = argv[3]
        self.checkerProcess = Checker(argv[4])
        self.timelimit = argv[5]
    
    def createFile(self, fileName: str, data: str) :
        f = open(_USER_DIRECTORY + "/" + fileName, "w")
        f.write(data)
        f.close()
    
    def run(self) :
        for i in range(1, self.nTest + 1) :
            print("- Test " + str(i) + " : ", end="")
            
            self.generator.run()
            if (self.generator.get_error() != None) :
                print("\n\t+", "Generator : ", self.generator.get_error())
                break
            dataInput = self.generator.stdout()
            self.createFile(_NAME_OF_INPUT, dataInput)
            
            
            self.solProcess.run(stdInput=dataInput, timelimit=self.timelimit)
            if (self.solProcess.get_error() != None) :
                print("\n\t+", "Solution : ", self.solProcess.get_error())
                print("\t+ Input : " + dataInput)
                break
            dataAnswer = self.solProcess.stdout()
            self.createFile(_NAME_OF_ANSWER, dataAnswer)
            
            
            self.codeProcess.run(stdInput=dataInput, timelimit=self.timelimit)
            if (self.codeProcess.get_error() != None) :
                print("\n\t+ Code : ", self.codeProcess.get_error())
                print("\t+ Input : " + dataInput)
                print("\t+ Answer : " + dataAnswer)
                break
            dataOutput = self.codeProcess.stdout()
            self.createFile(_NAME_OF_OUTPUT, dataOutput)
            
            
            output, returnCode = self.checkerProcess.run(stdInput=dataInput)
                
            print(output)
            if (returnCode != _RETURN_CODE_ACCEPT) :
                print("\t+ Input : " + dataInput)
                print("\t+ Output : " + dataOutput)
                print("\t+ Answer : " + dataAnswer)
                break
        
        Cleaner().run()