import math
import random
import winsound

print("Hello what is your name?")
person = input()
print("Okay", person, "welcome to the guessing game", "would you like to play?",
      "\n I will choose a number from a range of numbers you will input. Can you guess the number I choose?\n")

# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\nYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the right number!\n", 'Let the game begin\n')

# Initializing the number of guesses.
count = 0
# for calculation of minimum number of
# guesses depends upon random

while count < math.log(upper - lower + 1, 2):

    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if guess == x:
        winsound.PlaySound("YAY.wav", winsound.SND_LOOP)
        print("Congratulation", person, "you are the wiser and you did it in ", count, " try", "\U0001f600")
        exit()

    elif guess < x:
        print("You guessed too small!")
    elif guess > x:
        print("You guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    winsound.PlaySound("Boo.wav", winsound.SND_LOOP)
    print("\nThe guessing number was %d" % x)
    print("Sorry", person, "better luck next time!", "\U0001F606")




