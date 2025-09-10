import json

from quiz_data import get_random_question


def get_user_choice():
    while True:
        choice = input("Enter your answer(A/B/C/D): ").strip().upper()
        if choice in ['A','B','C','D']:
            return choice
        else:
            print("Invalid Input.")

def play_quiz_round():
    question,options,answer = get_random_question()

    print("\n" + question)
    for opt in options:
        print(opt)
    
    user_choice = get_user_choice()

    if user_choice == answer:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is {answer}")
        return 0

def load_score(filename="D:\\Python Based Mini Project\\Modular Mini Quiz Game\\quiz_game.json"):
    try:
        with open(filename,"r") as f:
            data = json.load(f)
            return data.get("score",0)
    
    except FileNotFoundError:
        return 0

def save_score(score,filename = "D:\\Python Based Mini Project\\Modular Mini Quiz Game\\quiz_game.json"):
    with open(filename,"w") as f:
        json.dump({"score":score},f)