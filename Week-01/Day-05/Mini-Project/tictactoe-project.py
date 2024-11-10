board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print("\n")

def player_input(player):
    while True:
        try:
            pos = int(input(f"Player {player}, enter your position (1-9): ")) - 1
            if pos in range(9) and board[pos] == " ":
                board[pos] = player
                break
            else:
                print("Invalid position. Choose an empty spot between 1-9.")
        except ValueError:
            print("Please enter a valid number between 1-9.")

def check_win():
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # win combinations in rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # win combinations in columns
        [0, 4, 8], [2, 4, 6]              # win combinations in diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None

def play():
    while True:
        board = [" " for _ in range(9)] #board reset with new game
        current_player = "X"
        turns = 0
        
        while turns < 9:
            display_board()
            player_input(current_player)
            
            winner = check_win()
            if winner:
                display_board()
                print(f"Player {winner} wins!")
                break
            
            current_player = "O" if current_player == "X" else "X"
            turns += 1

        if turns == 9 and not winner:
            display_board()
            print("The game is a tie!")

        play_again = input("Would you like to play again? (yes/no): ").strip()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

play()