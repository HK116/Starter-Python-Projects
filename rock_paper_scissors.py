"""
rock, paper, scissors game implementation.

this program allows a user to play rock, paper, scissors against the computer.
it keeps track of wins, losses, and ties until the user exits the game.
"""

import random
import sys

class RockPaperScissors:
    def __init__(self):
        print("welcome! let's play rock/paper/scissors")
        
        # dictionary mapping moves to corresponding emojis
        self.moves: dict = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
        
        # list of valid move strings
        self.valid_moves: list[str] = list(self.moves.keys())
        
        # counters for scores
        self.user_wins: int = 0
        self.computer_wins: int = 0
        self.ties: int = 0

    def play_game(self):
        # main game loop
        while True:
            user_move: str = input("rock, paper or scissors? >> ").lower()

            # exit condition
            if user_move == 'exit':
                self.display_score()
                print("thank you for playing! see you another time.")
                sys.exit()

            # check for valid move
            if user_move in self.valid_moves:
                # randomly choose computer's move
                computer_move: str = random.choice(self.valid_moves)
                
                # display moves and determine result
                self.display_moves(user_move, computer_move)
                result = self.check_moves(user_move, computer_move)

                # update score counters based on result
                if result == "computer wins!":
                    self.computer_wins += 1
                elif result == "you win!":
                    self.user_wins += 1
                elif result == "it's a tie.":
                    self.ties += 1

                print(result)
            else:
                print("invalid move...")

    def display_moves(self, user_move: str, computer_move: str):
        # display both moves using emojis
        print("----------------")
        print(f"you: {self.moves[user_move]}")
        print(f"computer: {self.moves[computer_move]}")
        print("----------------")

    def check_moves(self, user_move: str, computer_move: str) -> str:
        # determine game outcome based on moves
        if user_move == computer_move:
            return "it's a tie."
        elif (user_move == "rock" and computer_move == "paper") or \
             (user_move == "paper" and computer_move == "scissors") or \
             (user_move == "scissors" and computer_move == "rock"):
            return "computer wins!"
        else:
            return "you win!"
    
    def display_score(self):
        # display final scores upon exiting the game
        print(f"\nfinal scores:\n"
              f"you won {self.user_wins} times\n"
              f"computer won {self.computer_wins} times\n"
              f"it was a tie {self.ties} times\n")

# start the game if script is run directly
if __name__ == "__main__":
    rps = RockPaperScissors()
    rps.play_game()
