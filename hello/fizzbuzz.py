from ast import arg
import sys, getopt

first_input = (sys.argv[1])
second_input = (sys.argv[2])
third_input =  (sys.argv[3])
#i = (int(user_input))

for i in range (1,(int(first_input)) + 1):
    if (i % int(second_input) == 0) and (i % int(third_input) == 0):
        print(str(i) + "fizzbuzz")
    elif i % int(second_input) == 0:
        print(str(i) + "fizz")
    elif i % int(third_input) == 0:
        print(str(i) + "buzz")
    else :
        print(str(i))
