def print_board(board):
    print("\n" + "-" * 13)
    for row in board:
        print("| ", end="")
        print(" | ".join(row), end=" |\n")
        print("-" * 13)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(current_player, board):
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move < 9 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move! The cell is already occupied or out of range. Try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def play_game():
    board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_move(current_player, board)

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"\nPlayer {winner} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# اجرای بازی
play_game()
