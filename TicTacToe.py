import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def is_terminal(board):
    return is_winner(board, "X") or is_winner(board, "O") or is_draw(board)

def minimax(board, depth, is_maximizing, alpha, beta):
    if is_winner(board, "X"):
        return -10 + depth
    if is_winner(board, "O"):
        return 10 - depth
    if is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf

    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                eval = minimax(board, 0, False, alpha, beta)
                board[row][col] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (row, col)
    return best_move

def human_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter two numbers separated by a space.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    mode = input("Select game mode (1: Human vs. Computer, 2: Computer vs. Computer): ")
    if mode == "1":
        human_vs_computer(board)
    elif mode == "2":
        computer_vs_computer(board)
    else:
        print("Invalid mode. Exiting.")

def human_vs_computer(board):
    while not is_terminal(board):
        row, col = human_move(board)
        board[row][col] = "X"
        print_board(board)
        if is_terminal(board):
            break

        print("Computer's turn:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = "O"
        print_board(board)

    if is_winner(board, "X"):
        print("You win!")
    elif is_winner(board, "O"):
        print("Computer wins!")
    else:
        print("It's a draw!")

def computer_vs_computer(board):

    while not is_terminal(board):
        print("Computer X's turn:")
        best_move_x = find_best_move(board)
        board[best_move_x[0]][best_move_x[1]] = "X"
        print_board(board)
        if is_terminal(board):
            break

        print("Computer O's turn:")
        best_move_o = find_best_move(board)
        board[best_move_o[0]][best_move_o[1]] = "O"
        print_board(board)

    if is_winner(board, "X"):
        print("Computer X wins!")
    elif is_winner(board, "O"):
        print("Computer O wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()