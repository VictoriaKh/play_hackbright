"""A number-guessing game."""

# Put your code here
name = input("Howdy, what's is your name?")
print(name)


print(name,"I'm thinking of a number between 1 and 100.Try to guess my number.")

import random
num1 = random.randint(0,101)
ct = 0
while True:
    
    try:
        num = int(input("Your guess?"))
    except ValueError:
        print("That's not an int!")
        continue
    
    
    if num!=num1:
        ct = ct + 1
       
        if num<1 or num>100:
            print("invalid. enter between 1-100")
        if num in range(0,num1):
            print("Your guess is too low, try again.")
        elif num in range(num1+1,101):
            print("Your guess is too high, try again.") 
       

    else:
        print ("Well done,",name, "! You found my number in", ct, "tries!")                                                                      
        print("the random number was",num1)      
        break 