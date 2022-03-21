import random
number = random.randint(1,9)
guess = int(input("Enter your guess:"))
chances = 5
    
while guess != number:

    if guess < number:
        print("Sorry, but that guess was too low.")
    
    else:
        print("Sorry, but that guess was too high.")
        
    guess = int(input("Try again: "))

    if guess == number:
        print("Congratulations! You got the number! It was: ", number)