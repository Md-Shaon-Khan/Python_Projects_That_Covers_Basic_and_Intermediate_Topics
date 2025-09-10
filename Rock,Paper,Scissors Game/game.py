import random
from rps import get_winner

def play_game():
    print("------Rock, Paper, Scissors------")
    print("Type 'quit' to stop playing.\n")

    choices = ["rock","paper","scissors"]
    score = {
        "player": 0,
        "computer":0,
        "tie":0
    }

    while True:
        player_choice = input("Enter rock, paper or scissors: ").lower()

        if player_choice == "quit":
            print("\nFinal Score:")
            print(f"Player: {score['player']}, Computer: {score['computer']}, Ties: {score['tie']}")
            print("Thanks for playing!")
            break
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        winner = get_winner(player_choice, computer_choice)

        if winner == "player":
            print("You win this round!")
            score["player"] += 1
        elif winner == "computer":
            print("Computer wins this round!")
            score["computer"] += 1
        else:
            print("It's a tie!")
            score["tie"] += 1
        
        print(f"Score -> Player: {score['player']}, Computer: {score['computer']}, Ties: {score['tie']}\n")
