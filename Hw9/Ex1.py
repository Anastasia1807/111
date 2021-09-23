import random

secret_number = random.randrange(1,50)
print("Hello! Let's play in my favorit game!\nI thought of a number from 1 to 50, you have six attempts to guess it.\nGood luck! ")

for x in range(1,8):
    number = int(input("Try to guess the number: "))
    if number == secret_number:
        print("Well done! Right!")
        break
    elif x == 7:
        print("Game over! Goodbye!")
    else:
        print("You are wrong.Try again!")
    x += 1
