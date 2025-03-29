import random

NUM_ROUNDS = 5  # Number of rounds to play

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    score = 0  # Track player's score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        # Generate random numbers
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {player_number}")

        # Get user input and ensure it's valid
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Determine the result
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("You were right!", end=" ")
            score += 1  # Increase score
        else:
            print("Aww, that's incorrect.", end=" ")

        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")

    # Game Over - Display final message
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
