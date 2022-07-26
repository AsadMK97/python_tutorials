
def fibonacci():
    num1 = 0
    num2 = 1
    find = 2
    fibnum=0
    
    User = input("Enter a number")
    while find <= (int(User)):
        fibnum = (num1+num2)
        num1 = num2
        num2 = fibnum
        find = (find+1)
        continue
    print (fibnum)
        

fibonacci()