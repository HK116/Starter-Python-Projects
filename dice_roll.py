"""

"""

from random import randint

def roll_dice(value: int = 2) -> list[int]:
    if value <= 0:
        raise ValueError
    
    rolls: list[int] = []
    for i in range(value):
        rolls.append(randint(1, 6))
        
    return rolls

def main():
    while True:
        try:
            user_input: str = input("How many dice do you want to roll? ")

            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break 
            print(roll_dice(int(user_input)))

        except ValueError:
            print("Please a valid value. or 'exit' to quit.")

    
if __name__ == "__main__":
    main()