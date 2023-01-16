import os

compileOptions = {
    "cpp" : {
        "nt" : ["g++", "-O2", "$name$.cpp", "-o", "$name$.exe"],
        "posix" : ["g++", "-O2", "$name$.cpp", "-o", "$name$"]
    }
}

runOptions = {
    "cpp" : {
        "nt" : ["$name$.exe"],
        "posix" : ["./$name$"]
    },
    "py" : ["python3", "-u", "$name$"]
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

def get_run_options(language: str, fileName: str) -> list :
    if (len(compileOptions[language]) == 1) :
        runOption = runOptions[language]
    else :
        runOption = runOptions[language][os.name]
   
    ans = []
    for option in runOption :
        ans.append(option.replace("$name$", fileName))
    return ans