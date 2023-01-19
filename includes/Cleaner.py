import os
from includes.Initialize import _USER_DIRECTORY
from includes.Helper import *
from includes.Options import *

class Cleaner :
    def __init__(self) -> None:
        pass
    
    def run(self) : 
        for fileName in os.listdir(_USER_DIRECTORY) :
            if (get_language(fileName) in ["ans", "inp", "out"]) :
                continue
            if (get_language(fileName) in runOptions) :
                continue
            
            os.remove(_USER_DIRECTORY + "/" + fileName)
            