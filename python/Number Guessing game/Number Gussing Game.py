##Number guessing game
import random
try:
    print("Guess a number between 1 to 10")
    guess=int(input("Your Guess : "))
    number=random.randint(1,10)
    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10")
    elif guess < number:
        print("Guess is Low")
    elif guess > number:
        print("Guess is High")
    else:
        print("Congratulations! You guessed it!")
except ValueError:
    print("Please enter a valid number !")
