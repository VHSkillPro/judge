from includes.Process import *
from includes.Options import *

process = Process("code.cpp")
print(process.run("3").stdout.decode("utf-8"))
# print(get_compile_options("cpp", "SPLIT"))