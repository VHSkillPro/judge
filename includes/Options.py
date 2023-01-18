import os
from includes.Initialize import _USER_DIRECTORY

compileOptions = {
    "cpp" : {
        "nt" : ["g++", "-O2", _USER_DIRECTORY + '/' + "$name$.cpp", "-o", _USER_DIRECTORY + '/' + "$name$.exe"],
        "posix" : ["g++", "-O2", _USER_DIRECTORY + '/' + "$name$.cpp", "-o", _USER_DIRECTORY + '/' + "$name$"]
    }
}

runOptions = {
    "cpp" : {
        "nt" : [_USER_DIRECTORY + '/' + "$name$.exe"],
        "posix" : [_USER_DIRECTORY + "/$name$"]
    },
    "py" : {
        "nt" : ["python3", _USER_DIRECTORY + "/" + "$name$.py"],
        "posix" : ["python3", _USER_DIRECTORY + "/" + "$name$.py"]
    }
}

def have_compile(language: str) -> bool :
    return (language in compileOptions)

def get_compile_options(language: str, fileName: str) -> list :
    if (len(compileOptions[language]) == 1) :
        compileOption = compileOptions[language]
    else :
        compileOption = compileOptions[language][os.name]
   
    ans = []
    for option in compileOption :
        ans.append(option.replace("$name$", fileName))
        
    return ans

def get_run_options(language: str, fileName: str, argv: list = []) -> list :
    runOption = runOptions[language][os.name]
   
    ans = []
    for option in runOption :
        ans.append(option.replace("$name$", fileName))
        
    return ans + list(map(lambda x: str(x), argv))