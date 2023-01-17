from includes.Process import *
from includes.Options import *
from includes.Generator import *

process = Process("code.cpp")
generator = Generator("gen.cpp")

print(generator.run().stdout.decode("utf-8"))
# print(process.run("3", [23, "54"]).stdout.decode("utf-8"))
# print(get_run_options("cpp", "SPLIT", [2345, "34", "123"]))
