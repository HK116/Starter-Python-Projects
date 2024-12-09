import random

# generates a random number with unique digits from 100 to 999
def generate_unique_num() -> int:
    while True:
        num: int = random.randint(100, 999)
        if len(set(str(num))) == 3:
            return num

# prompts the user for a valid guess
def get_guess() -> int | None:
    while True:
        guess: str = input("guess a number with 3 unique digits: \n\t -> ").strip().lower()

        if guess in ['quit', 'exit']:
            return None
        
        if guess.isdigit() and len(guess) == 3 and len(set(guess)) == 3:
            return int(guess)
     
        print("invalid input. please enter a number with 3 unique digits.")

# main game loop
def game(target: int) -> None:
    if target is None:
        print("game setup failed. exiting.")
        return
    
    tries: int = 0
    while True:
        guess: int | None = get_guess()
        if guess is None:
            print("game exited. better luck next time!")
            return
        
        tries += 1
        if guess == target:
            print(f"you guessed the number {target} in {tries} tries!")
            return
        
        hint: str = "higher" if guess < target else "lower"
        print(f"target is {hint}. try again!")

# entry point
def main() -> None:
    print("to exit type: 'quit' or 'exit' \n")
    target: int = generate_unique_num()
    game(target)

if __name__ == "__main__":
    main()
