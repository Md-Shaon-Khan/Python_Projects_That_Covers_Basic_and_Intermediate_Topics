from number_genarating import number_genarating_game


def start_The_game():
    attempts = 0
    number = number_genarating_game()
    while True:
        try:
             guess = int(input("Enter your guess (1-100): "))
             attempts += 1

             if guess < 1 or guess > 100:
                 print("Out of range!Please guess between 1 and 100")
             elif guess < number:
                 print("Too low!Try again.")
             elif guess > number:
                 print("Too high!Try again.")
             else:
                 print(f"Correct!The number was {number}.")
                 print(f"You guessed it in {attempts} attempts.")
                 break
    
        except ValueError:
             print("Invalid input!Please enter an integer between the correct range.")

