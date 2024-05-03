def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 7)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    return True

def reset_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def tic_tac_toe():
    board = reset_board()
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That position is already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        tic_tac_toe()

if __name__ == "__main__":
    tic_tac_toe()
