import subprocess
from includes.Helper import *
from includes.Options import *

class Process :
    def __init__(self, filePath: str) -> None:
        self.filePath = filePath.strip()
        self.fileName = filePath[filePath.rfind('/') + 1::]
        self.compiled = False

    def compile(self) :
        if (not have_compile(get_language(self.fileName)) or self.compiled) :
            return 
        self.compiled = True
        return subprocess.run(
            get_compile_options(get_language(self.fileName), 
            get_name_without_extension(self.fileName)), 
            check=True
        )

    def run(self, stdInput : str = None, argv : list = []) :
        self.compile()
        if (stdInput != None) : 
            stdInput = stdInput.encode("utf-8")
                
        return subprocess.run(
            get_run_options(get_language(self.fileName), 
            get_name_without_extension(self.fileName), argv), 
            check=True, 
            capture_output=True, 
            input=stdInput
        )