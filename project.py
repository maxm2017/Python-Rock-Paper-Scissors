import random

#vars for the answer selection loop, the users answer, the opponents answer, and list of choices 
selected = False
answer = " "
opponentsChoice = " "
choices = ["Rock", "Paper", "Scissors"]

while True:

    #A while loop that will repeat until the user gives a valid answer 
    while selected==False:
        print("Pick Rock, Paper, or Scissors")
        answer = input()
        answer = answer.lower()
        if answer in choices:
            selected = True
        else:
            print("Invalid answer")

    # set selected back to false for the next round 
    selected = False

    #randomly select a choice for the oppononent 
    opponentsChoice = random.choice(choices)
    print(f"Your oponnents choice is: {opponentsChoice}")
    opponentsChoice = opponentsChoice.lower()


    #logic to see who wins the game
    result = " "
    if answer == "rock" and opponentsChoice == "paper":
        result = "loss"
    elif answer == "scissors" and opponentsChoice == "rock":
        result = "loss"
    elif answer == "paper" and opponentsChoice == "scissors":
        result = "loss"
    elif opponentsChoice== "rock" and answer == "paper":
        result = "win"
    elif opponentsChoice == "scissors" and answer == "rock":
        result = "win"
    elif opponentsChoice == "paper" and answer == "scissors":
        result = "win"
    else:
        result = "draw"

    print(f"Result: {result}")


    # give the user the chance to play again, if Y is entered to back to start of loop, else break
    print("Enter Y to play again, enter anything else to quit: ")
    answer = input()
    answer = answer.lower()
    print(answer)
    if answer != "y":
        break

