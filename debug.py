from includes.Process import *
from includes.Generator import *

process = Process("user/code1.cpp")
process.run(stdInput="123")
print(process.get_error())
