import random

def main():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    while True:
        try:
            # Get user's guess
            guess = int(input("Enter a guess: "))
            
            # Check if the guess is too low, too high, or correct
            if guess < secret_number:
                print("Your guess is too low")
            elif guess > secret_number:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == '__main__':
    main()
