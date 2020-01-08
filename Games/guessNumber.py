import random
num=int(input("Generate a random number from 1 to: "))
n=int(random.randint(1, num))
guess = int(input("Enter an integer from 1 to "+str(num)))
while n != "guess":
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to "+str(num)))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to "+str(num)))
    else:
        print ("you guessed it!")
        break