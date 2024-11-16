from game import Game

def get_user_menu_choice():
    """
    Display the menu and get the user's choice.
    """
    print("\nMenu:")
    print("1. Play a new game (Choose from rock, paper, scissors, lizard, spock)")
    print("2. Show scores")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ").strip()
    while choice not in ['1', '2', '3']:
        print("Invalid choice. Please select 1, 2, or 3.")
        choice = input("Enter your choice (1/2/3): ").strip()
    
    return choice

def print_results(results):
    """
    Print a summary of all the games played.
    """
    print("\nGame Summary:")
    print(f"Wins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("Thank you for playing!")

def main():
    """
    Main function to run the extended game.
    """
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        user_choice = get_user_menu_choice()
        
        if user_choice == '1':  # Play a new game
            print("\nPlaying Rock-Paper-Scissors-Lizard-Spock!")
            print("Choices: rock, paper, scissors, lizard, spock")
            game = Game()
            result = game.play()
            results[result] += 1
        elif user_choice == '2':  # Show scores
            print_results(results)
        elif user_choice == '3':  # Quit
            print_results(results)
            break

if __name__ == "__main__":
    main()