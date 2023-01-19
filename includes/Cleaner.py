import os
from includes.Initialize import _USER_DIRECTORY
from includes.Helper import *
from includes.Options import *

class Cleaner :
    def __init__(self) -> None:
        pass
    
    def run(self) : 
        for fileName in os.listdir(_USER_DIRECTORY) :
            if (get_language(fileName) in [None, "exe"]) :
                if (os.path.isfile(_USER_DIRECTORY + "/" + fileName)) :
                    os.remove(_USER_DIRECTORY + "/" + fileName)
            