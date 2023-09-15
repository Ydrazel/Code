#-*- code: utf-8 -*-
import sys

#try:
#    print("hello, my name is", sys.argv[1])
#    #Giving "0" to sys.argv as adress prints "name.py" as name
#except IndexError:
#    print("Too few arguments")

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# 
# print("hello. my name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
