from dice import roll_dice


def play_game():
    print("---------Welcome to Dice Rolling Game---------")

    while True:
        choice = input("Press 'r' to roll the dice or 'q' to quit: ").lower()

        if choice == "q":
            print("Exiting game.Thanks for playing!")
            break

        elif choice== "r":
            dice1 = roll_dice()
            dice2 = roll_dice()

            total = dice1 + dice2

            print(f"You rolled: {dice1} and {dice2} , (Total = {total} )")

            if total in(7,11):
                print("Congratulations!You Win.........")
            elif total in(2,3,12):
                print("Sorry!You lose...")
            else:
                print("Try again!Keep Rolling...")
        
        else:
            print("Invalid input!Please press 'r' to roll or 'q' for quit.")

