"""
__author__ = "Stephanie Wagley"
This is a Disney trivia game.
"""
# The basic outline of the game is from a Youtube video
# https://www.youtube.com/watch?v=l90vKQMDHPU&t=741s

print("Hello! Welcome to this Disney Trivia Game!")
print("Test your knowledge about all things Disney!")
print(10 ** 2)
# Instructions for the player.
print("INSTRUCTIONS")
print("Please enter all your answers in lowercase letters when necessary.")
print("Enter your answers using numbers when necessary.")
print("Have fun!")
print("*******************************************************************")

# Only works if the answer is lowercase.
# This won't go away until the user inputs y.
question = input("Do you want to play? [Y/N] ")
while question == "n":
    print("Wrong answer. Try again")
    question = input("Do you want to play? [Y/N] ")
    if question == "y":
        print("Let's begin!")


def win():
    """
    This is a message for the player at the end of the game based on if they
    answered all the questions correctly.
    :return:
    """
    if q1 == "f" and answer == 1955 and answer2 == 28:
        print("Congratulations! You answered all of the questions correctly!")
    else:
        print("You did not get all the questions correct. :( ")
        print("Just keep swimming and you'll get it next time!")


# Part of tis code is from https://www.101computing.net/number-only/
def q2(question):
    """
    This is the second question of the game.
    :return:
    """
    while True:
        try:
            q2 = int(input("2. What year did Disneyland open? "))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            return q2


# Part of this code is from https://www.101computing.net/number-only/
def q3(question):
    """
    This is the third question of the game.
    :return:
    """
    while True:
        try:
            q3 = int(input("3. What is Space Mountain's top speed? "))
        except ValueError:
            print("Not an integer. Try again.")
        else:
            return q3


q1 = input("1. Snow White and the Seven Dwarves was Walt Disney's "
           "favorite movie. [T/F] ")
if q1 == "t":
    print("No, the correct answer is Dumbo.")
if q1 == "f":
    print("Correct! Walt Disney's favorite movie was Dumbo.")

answer = q2("2. What year did Disneyland open?")
if answer == 1955:
    print("Hot dog!")
else:
    print("Sorry, the correct  answer is 1955.")

answer2 = q3("3. What is Space Mountain's top speed?")
if answer2 == 28:
    print("Hakuna matata!")
else:
    print("No, the correct answer is 28mph.")

# This is where the player's message comes up
win()

# This prints the number of smiley faces the user inputs.
# It also prints a sad face if the user inputs zero.
questions_correct = int(input("How many questions did you get correct? "))
for row in range(questions_correct):
    print(":)" + " ", end=" ")
if questions_correct == 0:
    print(":(")
