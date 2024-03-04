print('welcome to my first project')

question = input("Do you want to play? ")
score = 0

if question.lower() != "yes":
    quit()
else:
    print('lets play :) ')

question = input("where is Ethiopia located? ")

if question.lower() == "africa":
    print('Correct!')
    score += 1
else:
    print("Incorrect")

question = input("what language does ethiopians use? ")

if question.lower() == "amharic":
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
