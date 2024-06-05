# 4. Python's Random Game Night
# Objective:
# The aim of this assignment is to explore the random package in Python and understand how it can be used with loops to introduce randomness into your programs.

# Task 1: Random Choice Game
# Create a game where a player has a list of items. They have to guess which item in the list was selected. Use random.choice() to select the item and take the user's guess via input. Provide feedback on whether they guessed correctly or not.

import random

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count_guess = 0

for i in number:
    answer = random.choice(number)
    guess = int(input("Guess how many bunnies were seen today, between 1 and 10: "))
    count_guess += 1
    if guess == answer:
        print("Yay! You guessed the right number of bunnies!")
        break
    elif count_guess > 2:
        print("You lost!")
        break
    else:
        print("Try again!")
