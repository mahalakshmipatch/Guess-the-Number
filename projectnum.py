# Number game 
from random import randint

points=10

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

for i in range(0,10):
        guess = int(input("Enter your number: "))
        print("")
        print(f"Total Points: {points}")
        print("")
        if(guess==generatedNum):
            print("Your guess is right.")
            break
        else:
            print("Your guess was incorrect.")
            print("")
            points = points-1
            if(generatedNum>guess):
                print(f"Hint: Try quessing something bigger than {guess}.")
                print("")
                continue
            elif(generatedNum<guess):
                print(f"Hint: Try guessing something smaller than {guess}.")
                print("")
                continue