"""
Password Generator Program.

This program generates secure random passwords based on user preferences.
It supports options for including uppercase letters and symbols.
"""

import string
import secrets  # Secure random generator

def get_positive_int(prompt: str) -> int:
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Enter a non-negative integer!")
        except ValueError:
            print("Enter an integer!")

def get_yes_no(prompt: str) -> bool:
    """Get a yes/no response from the user."""
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "no"]:
            return response == "yes"
        print("Enter either 'yes' or 'no'")

def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    """Generate a secure random password based on user preferences."""
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    return ''.join(secrets.choice(combination) for _ in range(length))

def main():
    """Main function to handle user interaction and generate passwords."""
    print("Generate Passwords\n")

    num_of_pass = get_positive_int("How many passwords would you like to generate? ")
    has_uppercase = get_yes_no("Would you like your password to contain capital letters? (Yes/No) - ")
    has_symbols = get_yes_no("Would you like your password to contain symbols? (Yes/No) - ")

    print("-" * 24)
    for _ in range(num_of_pass):
        print(f"-> {generate_password(length=21, symbols=has_symbols, uppercase=has_uppercase)}") 
    print("-" * 24)

if __name__ == "__main__":
    main()
