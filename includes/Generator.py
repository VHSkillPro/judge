import time
from includes.Process import *
from includes.Initialize import _DEFAULT_MESSAGE_CE, _DEFAULT_MESSAGE_RE, _DEFAULT_MESSAGE_TLE, _RETURN_CODE_CE, _RETURN_CODE_RE, _RETURN_CODE_TLE

class Generator (Process):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
    
    def run(self):
        return super().run(argv=[time.time() * 10000])