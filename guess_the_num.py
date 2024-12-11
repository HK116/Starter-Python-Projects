"""
Number guessing game:

the program generates a random 3-digit number with unique digits.  
the player must guess the number by entering a valid 3-digit guess.  
after each incorrect guess, the program provides a hint:  
whether the target number is higher or lower than the guess.  
the game continues until the player guesses the correct number  
or types 'quit' or 'exit' to leave the game.
"""

from random import randint

# generates a random number with unique digits from 100 to 999
def generate_unique_num() -> int:
    while True:
        num: int = randint(100, 999)
        if len(set(str(num))) == 3:
            return num

# prompts the user for a valid guess
def get_guess() -> int | None:
    while True:
        guess: str = input("Guess -> ").strip().lower()

        if guess in ['quit', 'exit']:
            return None
        
        if guess.isdigit() and len(guess) == 3 and len(set(guess)) == 3:
            return int(guess)
     
        print("Invalid input. Please enter a number with 3 unique digits.")

# main game loop
def game(target: int) -> None:
    if target is None:
        print("Game setup failed, exiting.")
        return
    
    tries: int = 0
    while True:
        guess: int | None = get_guess()
        if guess is None:
            print("Game exited. Better luck next time!")
            return

        if tries > 9:
            print("Too many guesses! Game Over.")
            return
        
        tries += 1
        if guess == target:
            print(f"You guessed the number {target} in {tries} tries!")
            return
        
        hint: str = "higher" if guess < target else "lower"
        print(f"Target is {hint}. try again! Try # {tries}")

# entry point
def main() -> None:
    print("To exit type: 'quit' or 'exit' \n")
    print("Guess a number with 3 unique digits in under 10 tries")
    target: int = generate_unique_num()
    game(target)

if __name__ == "__main__":
    main()
