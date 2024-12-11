"""
This program simulates rolling dice. It asks the user how many dice to roll, rolls that many six-sided dice, 
and prints the results. The user can type 'exit' to quit the program.
"""
from random import randint

def roll_dice(value: int = 2) -> list[int]:
    """Rolls the specified number of six-sided dice and returns the results as a list of integers."""

    if value <= 0:
        raise ValueError
    
    return [randint(1, 6) for _ in range(value)]


def main():
    """Main loop for user interaction, allowing repeated dice rolls or exiting the program."""

    while True:
        user_input: str = input("How many dice do you want to roll? ")
        
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break 

        try:
            num_dice = int(user_input)
            rolls = roll_dice(num_dice)

            print(*rolls, sep=", ", end=" ")
            print(f"({sum(rolls)})")

        except ValueError:
            print("Please a valid value. or 'exit' to quit.")

    
if __name__ == "__main__":
    main()