print('welcome to my first project')

question = input("Do you want to play? ")
score = 0

if question.lower() != "yes":
    quit()
else:
    print('lets play :) ')

question = input("Write the name of GOD? ")

if question.lower() == "jesus":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

question = input("By whose name the bible tell us to baptize? ")

if question.lower() == "jesus":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

question = input("Who am i? ")

if question.lower() == "elisha":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question = input("Where i will live? ")


if question.lower() == "us":
    print("Correct")
    score += 1
else:
    print("Incorrect")
print("You got " + str(score) + " answers correctly.")
print("You answered " + str((score/4) * 100) + " %")
