import sys
from includes.Process import *
from includes.Checker import *
from includes.Generator import *
from includes.Initialize import _NUMBER_OF_TEST, _USER_DIRECTORY, _NAME_OF_INPUT, _NAME_OF_OUTPUT, _NAME_OF_ANSWER, _DEFAULT_MESSAGE_ACCEPT, _DEFAULT_MESSAGE_WRONG

class Judge :
    def __init__(self) -> None:
        self.codeProcess = Process(sys.argv[1])
        self.solProcess = Process(sys.argv[2])
        self.generator = Generator(sys.argv[3])
        self.nTest = _NUMBER_OF_TEST if len(sys.argv) < 5 else int(sys.argv[4])
        self.checkerProcess = None if len(sys.argv) < 6 else Checker(sys.argv[5])
    
    def createFile(self, fileName: str, data: str) :
        f = open(_USER_DIRECTORY + "/" + fileName, "w")
        f.write(data)
        f.close()
    
    def run(self) :
        for i in range(1, self.nTest + 1) :
            print("Test " + str(i) + " : ", end="")
            
            dataInput = self.generator.run().stdout.decode("utf-8").strip()
            dataOutput = self.codeProcess.run(stdInput=dataInput).stdout.decode("utf-8").strip()
            dataAnswer = self.solProcess.run(stdInput=dataInput).stdout.decode("utf-8").strip()
            
            self.createFile(_NAME_OF_INPUT, dataInput)
            self.createFile(_NAME_OF_OUTPUT, dataOutput)
            self.createFile(_NAME_OF_ANSWER, dataAnswer)
            
            if (self.checkerProcess == None) :
                if (dataAnswer == dataOutput) :
                    output = _DEFAULT_MESSAGE_ACCEPT
                    returnCode = 0
                else :
                    output = _DEFAULT_MESSAGE_WRONG
                    returnCode = 1  
            else :
                checkerCompleteProcess = self.checkerProcess.run(stdInput=dataInput)
                output = checkerCompleteProcess.stdout.decode("utf-8")
                returnCode = checkerCompleteProcess.returncode
                
            print(output)
            if (returnCode != 0) :
                print("Input : ")
                print(dataInput)
                
                print("Output : ")
                print(dataOutput)
                
                print("Answer : ")
                print(dataAnswer)
                
                exit(0)