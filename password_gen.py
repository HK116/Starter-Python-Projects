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
            if value >= 1:  # Ensure the length is at least 1
                return value
            print("Enter a positive integer greater than 0!")
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
    password = []

    # Ensure the password contains at least one uppercase letter if requested
    if uppercase:
        password.append(secrets.choice(string.ascii_uppercase))

    # Ensure the password contains at least one symbol if requested
    if symbols:
        password.append(secrets.choice(string.punctuation))

    # Add the remaining characters randomly from the allowed pool
    remaining_length = length - len(password)
    if remaining_length > 0:
        # Add random characters to fill the rest of the password
        combination += string.ascii_uppercase if uppercase else ""
        combination += string.punctuation if symbols else ""
        password += [secrets.choice(combination) for _ in range(remaining_length)]

    # Shuffle the list to ensure randomness in the order of characters
    secrets.SystemRandom().shuffle(password)

    # Return the password as a string
    return ''.join(password)

def main():
    """Main function to handle user interaction and generate passwords."""
    print("Generate Passwords\n")

    num_of_pass = get_positive_int("How many passwords would you like to generate? ")
    password_length = get_positive_int("What length would you like your password to be? ")

    has_uppercase = get_yes_no("Would you like your password to contain capital letters? (Yes/No) - ")
    has_symbols = get_yes_no("Would you like your password to contain symbols? (Yes/No) - ")

    print("-" * 24)
    for _ in range(num_of_pass):
        print(f"-> {generate_password(length=password_length, symbols=has_symbols, uppercase=has_uppercase)}") 
    print("-" * 24)

if __name__ == "__main__":
    main()
