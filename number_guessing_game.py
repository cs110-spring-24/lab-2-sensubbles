import random
num = random.randint(1, 100)

user = input("Enter your guess: ")
user = int(user)

if user > num:
    print("Too high, it was", num)
elif user < num:
    print("Too low, it was", num)
else:
    print("You got it!")
