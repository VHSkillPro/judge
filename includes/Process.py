import subprocess
from includes.Helper import *
from includes.Options import *
from includes.Initialize import _COLOR_CE, _COLOR_RE, _COLOR_TLE, _DEFAULT_MESSAGE_CE, _DEFAULT_MESSAGE_RE, _DEFAULT_MESSAGE_TLE, _DEFAULT_TIME_LIMIT, _RETURN_CODE_ACCEPT, _RETURN_CODE_CE, _RETURN_CODE_TLE, _RETURN_CODE_RE, _STYLE_BRIGHT, _STYLE_RESET_ALL

class Process :
    def __init__(self, filePath: str) -> None:
        self.fileName = filePath.strip()[filePath.rfind('/') + 1::]
        self.compiled = False
        self.process = None
        self.returnCode = -1

    def compile(self) :
        """
            Return :
            - Compiled successfully = _RETURN_CODE_ACCEPT
            - Compiled error = _RETURN_CODE_CE
        """
        if (not have_compile(get_language(self.fileName)) or self.compiled) :
            return _RETURN_CODE_ACCEPT
        
        try :
            self.process = subprocess.run(
                get_compile_options(get_language(self.fileName), 
                get_name_without_extension(self.fileName)),
                check=True,
                capture_output=True
            )
            
            self.compiled = True
        except subprocess.CalledProcessError: 
            return _RETURN_CODE_CE
    
        return _RETURN_CODE_ACCEPT

    def run(self, stdInput : str = None, argv : list = [], timelimit : int = _DEFAULT_TIME_LIMIT) :
        """
            Parameters : 
                - stdInput (str) : standar input (Default = None)
                - argv (list) : list of argument (Default = [])
                - timelimit (int) : limit of time (Default = 1s)
                
            Return :
                - _RETURN_CODE_ACCEPT = execute successfully
                - _RETURN_CODE_RE = runtime error
                - _RETURN_CODE_TLE = time limit exceed
                - _RETURN_CODE_CE = compile error
        """
        self.returnCode = self.compile()
        if (self.returnCode != _RETURN_CODE_ACCEPT) :
            return self.returnCode
        
        if (stdInput != None) :
            stdInput = stdInput.encode("utf-8").strip()
        
        try :
            self.process = subprocess.run(
                get_run_options(get_language(self.fileName), 
                get_name_without_extension(self.fileName), argv),
                capture_output=True, 
                input=stdInput,
                timeout=timelimit
            )
        except subprocess.TimeoutExpired :
            self.returnCode = _RETURN_CODE_TLE
            return self.returnCode
        except subprocess.SubprocessError :
            self.returnCode = _RETURN_CODE_RE
            return self.returnCode
        
        if (self.process.returncode != _RETURN_CODE_ACCEPT) :
            self.returnCode = _RETURN_CODE_RE
            return _RETURN_CODE_RE
        
        self.returnCode = _RETURN_CODE_ACCEPT
        return _RETURN_CODE_ACCEPT

    def stdout(self) :
        return self.process.stdout.decode("utf-8").strip()
    
    def returncode(self) :
        return self.returnCode
    
    def get_error(self) :
        if (self.returncode() == _RETURN_CODE_RE) :
            return _STYLE_BRIGHT + _COLOR_RE + _DEFAULT_MESSAGE_RE + _STYLE_RESET_ALL
        if (self.returncode() == _RETURN_CODE_TLE) :
            return _STYLE_BRIGHT + _COLOR_TLE + _DEFAULT_MESSAGE_TLE + _STYLE_RESET_ALL
        if (self.returncode() == _RETURN_CODE_CE) :
            return _STYLE_BRIGHT + _COLOR_CE + _DEFAULT_MESSAGE_CE + _STYLE_RESET_ALL
        return None
    
    