# from includes.Process import *
# from includes.Options import *
# from includes.Generator import *
# from includes.Checker import *

# code = Process("code.cpp")
# sol = Process("sol.cpp")

# generator = Generator("gen.cpp")

# dataInput = generator.run().stdout.decode("utf-8")
# finp = open("user/data.inp", "w")
# finp.write(dataInput)
# finp.close()

# fout = open("user/data.out", "w")
# fout.write(code.run(stdInput=dataInput).stdout.decode("utf-8"))
# fout.close()

# fans = open("user/data.ans", "w")
# fans.write(sol.run(stdInput=dataInput).stdout.decode("utf-8"))
# fans.close()

# checker = Checker()
# print(checker.run().stdout.decode('utf-8'))

from includes.Judge import *

judge = Judge()
judge.run()
