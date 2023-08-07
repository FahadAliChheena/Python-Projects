import random

def play_number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty == "easy" else 5
    
    print(f"You have {attempts} attempts remaining to guess the number.\n")
    
    while attempts > 0:
        guess = get_user_guess()
        
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high.")
        else:
            print("Too low.")
        
        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining to guess the number.\n")
        else:
            print("You've run out of guesses, you lose.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Make a guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play_number_guessing_game()