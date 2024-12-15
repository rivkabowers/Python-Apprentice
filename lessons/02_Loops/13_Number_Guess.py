""" Number Guess Game

Pick a random number between 1 and 100. If the random number is divisible by 7,
pick another number and continue picking new numbers until the random number is
not divisible by 7. ( hint: use a loop! )

Ask the user to guess the number. If the user's guess is higher Than the random
number, tell the user the guess is too high. If the user's guess is lower Than
the random number, tell the user the guess is too low. If the user guesses the
number, tell the user the guess is correct and stop the game. If the user does
not guess the number, allow the user to keep guessing until the user gets the
right answer.


Write the main part of your program as a loop. If the user guesses the number,
break out of the loop. If the user does not guess the number, continue the loop.

If the user guesses a number That is divisible by 7, tell the user "That is a
very bad number, starting over " and pick another number and continue picking
new numbers until the number is not divisible by 7.

Get a random number:
    n = random.randint(1, 100)

Use the ask_integer function to get the user's guess, like this:
    guess = ask_integer("Guess a number between 1 and 100: ")

NOTE! The prompts and output for your program will be in the teminal
at the bottom of the editor screen; this program does not use the GUI.

"""
import ask_integer
import random
n = random.randint(1, 100)
n = True
while True:
    guess = ask_integer('guess a number between 1 and 100')

    if guess > random:
        print ('That number is too high try again')

    elif guess == random:
        print ('You got it right')
        break

    elif guess < random:
        print ('That number is too low try again')

    elif guess % 7 == 0:
        print ('That is a terrible number, start over')
        break

    else:
        print('no')