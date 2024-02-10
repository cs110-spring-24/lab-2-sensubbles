import random
num = random.randint(1, 100)
user = 0
guess = 0
upbound = 100
lowbound = 1

print("I'm thinking of a number between 1 and 100.")

while user != num:
    user = input("Enter your guess: ")
    user = int(user)
    if user > 100:
        print("Please enter a number that isn't greater than 100.")
    else:
        if user > num:
            if lowbound > upbound:
                lowbound = upbound
            elif upbound < lowbound:
                upbound = lowbound
            upbound = user - 2
            if user - 2 < upbound:
                upbound = user - 2
            if upbound < num:
                upbound = num
            print("Too high! It's between", lowbound, "and", upbound)
            guess = guess + 1
                
        elif user < num:
            if lowbound > upbound:
                lowbound = upbound
            elif upbound < lowbound:
                upbound = lowbound
            lowbound = user + 2
            if user + 2 > lowbound:
                lowbound = user + 2
            if lowbound > num:
                lowbound = num
            print("Too low! It's between", lowbound, "and", upbound)
            guess = guess + 1
        else:
            guess = guess + 1
            print("You got it! And it only took you", guess, "tries!")

        


