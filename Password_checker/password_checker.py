"""
This script checks how common a given password is by comparing it against a list
of common passwords. It reads a file containing popular passwords and returns
the rank of the password if it matches, or informs the user that the password
seems unique if no match is found. The script ensures the user enters a valid, non-empty password.
"""

def check_password(password: str):
    """
    Checks if the given password is in a list of common passwords and prints the result.

    Args:
        password (str): The password to be checked against the common passwords list.
    """
    # Open the file containing common passwords and read the list
    with open('passwords.txt', 'r') as file:
        common_passwords: list[str] = file.read().splitlines()

    # Iterate over the list of common passwords and check if the input password matches
    for i, psswrd in enumerate(common_passwords):
        if password == psswrd:
            # If a match is found, print the rank and indicate it's common
            print(f"{password}: ❌ (Rank by commonality: #{i + 1})")  # i + 1 for user-friendly rank
            return
    
    # If no match is found, print that the password seems unique
    print(f"No match, {password} is not common ✅")


def main():
    """
    Main function to execute the script. Prompts the user for a password and checks its
    commonality by calling the check_password function. Ensures the user enters a valid password.
    """
    while True:
        # Ask the user for the password they want to check
        password = input("Enter a password to check: ").strip()
        
        # Check if the password is not empty
        if password:
            # Call check_password to verify how common the entered password is
            check_password(password)
            break  # Exit the loop after a valid password is entered
        else:
            # Inform the user if the input is empty or just spaces
            print("Password cannot be empty. Please enter a valid password.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
