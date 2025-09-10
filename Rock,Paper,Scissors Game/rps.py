def get_winner(player_choice:str , computer_choice:str) -> str:
    if player_choice == computer_choice:
        return "tie"
    
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if rules[player_choice] == computer_choice:
        return "player"
    else:
        return "computer"