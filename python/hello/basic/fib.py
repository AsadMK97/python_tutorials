def fibonacci():
    num1 = 0
    num2 = 1
    find = 2
    fibnum = 0
    endnum = 10

    while find <= endnum:
        fibnum = num1 + num2
        num1 = num2
        num2 = fibnum
        find = find + 1
        continue
    print(fibnum)


# user_input = input("Enter a number: ")
# fibnum = fibonacci(user_input)
fibonacci()
