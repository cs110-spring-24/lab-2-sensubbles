import random

num = random.randint(1, 100)
user = 0
guess = 0
lowbound = 1
upbound = 100

print(f"I'm thinking of a number between 1 and {upbound}.")

while user != num:
    user = int(input("Enter your guess: "))

    if user > upbound:
        print(f"Please enter a number that's between 1 and {upbound}")
    elif user > num:
        upbound = user - 1  # Update upper bound to one less than guess
        print(f"Too high! It's between {lowbound} and {upbound}")
        guess += 1
    elif user < num:
        lowbound = user + 1  # Update lower bound to one more than guess
        print(f"Too low! It's between {lowbound} and {upbound}")
        guess += 1
    else:
        guess += 1
        print(f"You got it! And it only took you {guess} tries!")

