import sys

file_out = sys.argv[1]
file_ans = sys.argv[2]

if (open(file_out).read().strip() == open(file_ans).read().strip()) :
    print("Accept !!!")
    exit(0)
else :
    print("Wrong !!!")
    exit(1)