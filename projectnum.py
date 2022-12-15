# Number game 
from random import randint

answer = True
points=100

level = input("What level would you like to play? Easy/Medium/Hard: ")

if(level=="Easy"):
    generatedNum = randint(1,100)
    print("Guess a number between 1-100")
elif(level=="Medium"):
    generatedNum = randint(1,1000)
    print("Guess a number between 1-1000")
elif(level=="Hard"):
    generatedNum = randint(1,100000)
    print("Guess a number between 1-100000")
else:
    print("Invalid Input")

while(answer==True):
    guess = int(input("Enter your number: "))
    print("")
    print(f"Total Points: {points}")
    print("")
    if(guess==generatedNum):
        print("Your guess is right.")
        answer = False
    else:
        print("Your guess was incorrect.")
        print("")
        points = points-1
        if(generatedNum>guess):
            print("Hint: Try quessing something bigger.")
            print("")
            continue
        elif(generatedNum<guess):
            print("Hint: Try guessing something smaller.")
            print("")
            continue