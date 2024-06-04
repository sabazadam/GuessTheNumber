from logo import logo
from random import randint
def gameStart():
    global health
    while health > 0:
        guessNumber = int(input("Make a guess: "))
        if guessNumber > randomNumber:
            health -= 1
            print("Too High!")
            print("Guess Again.")
            print(f"You have {health} attempts remaining to guess the number.")

        elif guessNumber < randomNumber:
            health -= 1
            print("Too low!")
            print("Guess Again.")
            print(f"You have {health} attempts remaining to guess the number.")

        else:
            print("Well done you win!")
            return
    print("YOU LOSE! Try again")
print(logo)

print("Welcome to the game!")
health = 0
shouldContinue = True
while shouldContinue:
    randomNumber = randint(1, 100)
    response = input("Please select level! Type 'easy' to play easy and type 'hard' to play hard. Also type 'q' to exit: ")
    if response == "easy":
        health = 10
        gameStart()
    elif response == "hard":
        health = 5
        gameStart()
    elif response == "q":
        shouldContinue = False
        print("BYE!")
    else:
        print("invalid input!")
        continue
