import time
from includes.Process import *

class Generator (Process):
    def __init__(self, filePath: str) -> None:
        super().__init__(filePath)
    
    def run(self):
        return super().run(argv=[time.time()])