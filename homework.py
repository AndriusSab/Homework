# Ideas:

#  Akmuo, lapas, žirklės 

# Requirements: OOP (Inheritance as minimum), functions, modules, import, types, clean code , naming, logging.

import random

class Game:
    def __init__(self):
        self.user_action = None
        self.possible_actions = ["rock", "paper", "scissors"]
        self.computer_action = None
    
    def get_user_choice(self):
        while True:
            try:
                user_input = input("Enter a choice (rock, paper, scissors): ").lower()
                if not user_input  in self.possible_actions:
                    raise ValueError("Invalid input. Please enter rock, paper, or scissors.")
                self.user_action = user_input
                break
            except ValueError as e:
                print(e)
    
    def get_computer_action(self):
        self.computer_action = random.choice(self.possible_actions)
    
    def determine_winner(self):
        if self.user_action == self.computer_action:
            print(f"Both players selected {self.user_action}. It's a tie!")
        elif self.user_action == "rock":
            if self.computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif self.user_action == "paper":
            if self.computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif self.user_action == "scissors":
            if self.computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
    
    def play(self):
        while True:
            self.get_user_action()
            self.get_computer_action()
            print(f"\nYou chose {self.user_action}, computer chose {self.computer_action}.\n")
            self.determine_winner()
            play_again = input("Play again? (y/n): ").lower()
            if play_again != "y":
                break

game = Game()
game.play()