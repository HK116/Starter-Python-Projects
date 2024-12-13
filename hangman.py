"""
Hangman Game

This is a simple implementation of the classic hangman game.
The player guesses letters to uncover a hidden word chosen at random.
They have a limited number of tries before the game ends.

Features:
- Random word selection from a predefined list.
- Interactive prompts for guessing letters
- Displays current progress after each guess
- Alerts when a guess is repeated or incorrect
- Ends game when the word is guessed or tries run out

Enjoy playing!

"""

from random import choice

def get_random_word() -> str:
    """Returns a random word from a predefined list."""
    return choice(["apple", "banana", "choice", "secret", "happy", "sad", "easy"])

def display_word_progress(word: str, guessed: str) -> str:
    """Returns the current state of the word with guessed letters revealed."""
    return ''.join([char if char in guessed else '_' for char in word])

def get_user_guess(guessed: str) -> str:
    """Prompts the user for a guess and ensures it's not a repeated letter."""
    while True:
        guess: str = input("Enter a letter: ").lower()
        if guess in guessed:
            print(f"You already guessed {guess}. Try another letter!")
        elif len(guess) > 1:
            print("Please enter a single letter!")
        else:
            return guess

def run_game():
    """Main function to run the hangman game."""
    word: str = get_random_word()
    username: str = input("What is your name? ").capitalize()
    print(f"Welcome to hangma, {username}!")
          
    guessed: str = ''
    tries: int = 5

    while tries > 0:
        current_progress = display_word_progress(word, guessed)
        print(f"Word: {current_progress}")
              
        if "_" not in current_progress:
            print("Congrats, you got it!")
            break

        guess = get_user_guess(guessed)
        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Wrong guess! Tries left: {tries}")
            if tries == 0:
                print(f"Game Over! The word was {word}")
                break
    
if __name__ == "__main__":
    run_game()