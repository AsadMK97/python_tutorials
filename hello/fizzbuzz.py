import sys

for i in range(1, 20):
    if (i % 4 == 0) and (i % 3 == 0):
        print(str(i) + "fizzbuzz")
    elif i % 3 == 0:
        print(str(i) + "fizz")
    elif i % 4 == 0:
        print(str(i) + "buzz")
    else :
        print(str(i))



