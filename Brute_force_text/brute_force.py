"""
Password guessing script for educational purposes only.

This script demonstrates common word matching and brute-force password guessing.
CAUTION: Unauthorized password guessing can be illegal and is strictly prohibited.
Use this script for educational and learning purposes only.
"""

import itertools  # For generating combinations of characters
import string     # For character sets
import time       # For tracking execution time


def common_guess(word: str) -> str | None:
    """Check if the word exists in a common password list."""
    try:
        with open("words.txt", "r") as file:
            word_list: list[str] = file.read().splitlines()
            
            # Enumerate through the list to find a match
            for i, match in enumerate(word_list, start=1):
                if match == word:
                    return f"Common match: {match} (# {i})"
    except FileNotFoundError:
        return "Error: words.txt not found."


def brute_force(word: str, length: int, has_digits: bool = False, has_symbols: bool = False) -> str | None:
    """Attempt to brute-force the password using specified character sets."""
    chars: str = string.ascii_lowercase

    # Add digits and symbols if specified
    if has_digits:
        chars += string.digits
    if has_symbols:
        chars += string.punctuation

    attempts: int = 0

    # Generate combinations of characters of the given length
    for guess_tuple in itertools.product(chars, repeat=length):
        attempts += 1
        guess: str = "".join(guess_tuple)

        # Check if the generated guess matches the word
        if guess == word:
            return f"{word} was cracked in {attempts:,} guesses."

    return None


def main():
    """Main execution function for the password guessing process."""
    print("Searching...")
    password: str = 'henok'

    # Start timing the process
    start_time: float = time.perf_counter()

    # First, check common password list
    if common_match := common_guess(password):
        print(common_match)
    else:
        # If not found, attempt brute-forcing
        if cracked := brute_force(password, length=5, has_digits=False, has_symbols=False):
            print(cracked)
        else:
            print("There was no match...")

    # Calculate and display elapsed time
    end_time: float = time.perf_counter()
    print(round(end_time - start_time, 2), 's')


if __name__ == "__main__":
    main()
