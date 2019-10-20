# Stephanie Wagley
# A trivia game

print("Hello! Welcome to this Disney Trivia Game!")
print("Test your knowledge about all things Disney!")
print(10 ** 2)

question = input("Do you want to play? [Y/N]")
while question == "n":
    print("Wrong answer. Try again")
    question = input("Do you want to play? [Y/N]")
    if question == "y":
        print("Let's begin!")

def win():
    if q1 == "f" and q2 == 1955 and q3 == 28:
        print("Congratulations! You answered all of the questions correctly!")
    else:
        print("Just keep swimming and you'll get it next time!")


q1 = input("1. Snow White and the Seven Dwarves was Walt Disney's favorite movie. [T/F]")
if q1 == "t":
    print("No, the correct answer is Dumbo.")
if q1 == "f":
    print("Correct! Walt Disney's favorite movie was Dumbo.")

q2 = int(input("2. What year did Disneyland open?"))
if q2 == 1955:
    print("Hot dog!")
else:
    print("Sorry, the correct  answer is 1955.")

q3 = int(input("3. What is Space Mountain's top speed?"))
if q3 == 28:
    print("Hakuna matata!")
else:
    print("No, the correct answer is 28mph.")


win()

qCorrect = int(input("How many questions did you get correct?"))
for row in range(qCorrect):
    print(":)" + " ", end=" ")
if qCorrect == 0:
    print(":(")
