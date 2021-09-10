import random

#vars for the answer selection loop, the users answer, the opponents answer, and list of choices 
selected = False
answer = " "
opponentsChoice = " "
choices = ["rock", "paper", "scissors", "lizard", "spock"]

#Dictionary defining which choice wins against which 
winsAgainst = {
    "rock": ["scissors","lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper","lizard"],
    "lizard": ["paper", "spock"],
    "spock" : ["scissors", "rock"]
}

while True:

    #A while loop that will repeat until the user gives a valid answer 
    while selected==False:
        print(f"Pick  from {choices}")
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
    print(f"Your opponents choice is: {opponentsChoice}")

    #Decides a draw if player and opponent choices match 
    if answer == opponentsChoice:
        result = "draw"

    #checks each entry in the dictionary to see if the player has won against opponent, sets result to win if so, loss if not 
    for winner, losers in winsAgainst.items():
        if answer == winner and opponentsChoice in losers:
            result = "win"
            break
        result = "loss"

    print(f"Result: {result}")

    # give the user the chance to play again, if Y is entered to back to start of loop, else break
    print("Enter Y to play again, enter anything else to quit: ")
    answer = input()
    answer = answer.lower()
    print(answer)
    if answer != "y":
        break

