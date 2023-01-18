from includes.Process import *
from includes.Checker import *
from includes.Generator import *
from includes.Argument import *
from includes.Cleaner import *
from includes.Initialize import _USER_DIRECTORY, _NAME_OF_INPUT, _NAME_OF_OUTPUT, _NAME_OF_ANSWER, _DEFAULT_CHECKER

class Judge :
    def __init__(self) -> None:
        argv = Argument().get_argument()

        self.codeProcess = Process(argv[0])
        self.solProcess = Process(argv[1])
        self.generator = Generator(argv[2])
        self.nTest = argv[3]
        self.checkerProcess = Checker(argv[4])
    
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
            
            output, returnCode = self.checkerProcess.run(stdInput=dataInput)
                
            print(output)
            if (returnCode != 0) :
                print("Input : ")
                print(dataInput)
                
                print("Output : ")
                print(dataOutput)
                
                print("Answer : ")
                print(dataAnswer)
                
                exit(0)
        
        Cleaner().run()