from quiz_functions import play_quiz_round, load_score, save_score

def main():
    print("Welcome to the Mini Quiz Game!")
    score = load_score()
    print(f"Your current score: {score}")
    while True: 
        print("\n1. Play Quiz\n2. Exit") 
        choice = input("Choose an option: ").strip()
        if choice == "1":
            score += play_quiz_round() 
            print(f"Your score: {score}")
            save_score(score)
        elif choice == "2":
            print(f"Thanks for playing! Final score: {score}")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()