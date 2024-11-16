import random

class Game:
    def __init__(self):
        """
        Initialize the game with the possible choices.
        """
        self.choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    def get_user_item(self):
        """
        Ask the user to select an item. Validate input.
        """
        user_item = None
        while user_item not in self.choices:
            user_item = input(f"Choose one ({', '.join(self.choices)}): ").lower()
            if user_item not in self.choices:
                print("Invalid choice. Please try again.")
        return user_item

    def get_computer_item(self):
        """
        Select a random choice for the computer.
        """
        return random.choice(self.choices)

    def get_game_result(self, user_item, computer_item):
        """
        Determine the result of the game based on the extended rules.
        """
        winning_combinations = {
            'scissors': ['paper', 'lizard'],
            'paper': ['rock', 'spock'],
            'rock': ['lizard', 'scissors'],
            'lizard': ['spock', 'paper'],
            'spock': ['scissors', 'rock']
        }

        if user_item == computer_item:
            return "draw"
        elif computer_item in winning_combinations[user_item]:
            return "win"
        else:
            return "loss"

    def play(self):
        """
        Play a single round of Rock-Paper-Scissors-Lizard-Spock.
        """
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"You selected {user_item}. The computer selected {computer_item}.")
        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")
        
        return result