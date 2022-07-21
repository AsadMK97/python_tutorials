
name = input("What is your name?")
age = input("How old are you?")

print ("Your name is "+ name +" and you are " + age)

age = int(age)

print(type(age)) #Checks if input has changed to integer correctly

london_calcuator = age - 23
london_calcuator = str(london_calcuator) #Changes integer back to string.

print("You were "+ london_calcuator +" years old when the london eye opened in 1999")