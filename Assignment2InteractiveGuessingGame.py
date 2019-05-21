import random

randomnumber = random.randint(1,10)
print(randomnumber)

for i in range (1,4):
    userguess = input("What number do you guess?")
    userguess = int(userguess)
    if randomnumber == userguess:
        print("Congradulation! Your guess is correct!")
        break
    elif randomnumber < userguess:
        print("Sorry, your guess is too high!")
    else:
        print("Sorry, your guess is too low!")


