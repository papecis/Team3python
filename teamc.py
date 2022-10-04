import random
import math
import winsound

person = input('Enter your name: ')
print('Hello', person)
print("Welcome to the guessing game!")
# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), "chances to guess the right number!\n")

# Initializing the number of guesses.
count = 0
# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations", person, "you are the wiser and you did it in", count, "try", "\U0001f600")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    winsound.PlaySound("BOO.wav", winsound.SND_LOOP)
    print("\nThe guessing number was %d" % x)
    print("\tBetter Luck", person, "the next time!", "\U0001F606")



