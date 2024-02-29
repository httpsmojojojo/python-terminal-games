from random import randint

randomnumber = randint (0,10)
print("Enter any number from 0 to 10") 

x = -1

while x != randomnumber:
    if x != -1:
        print("Wrong guess")

    x = input("Enter a number: ")
    x = int(x)
    

print("You guessed correctly")
