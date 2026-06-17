import math

# Initialize board
board = [" " for _ in range(9)]

# Print board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print("\n")

# Check winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(b[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw(b):
    return " " not in b

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):  # AI
        return 1
    if check_winner(b, "X"):  # Human
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Human move
def human_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if board[pos] == " ":
                board[pos] = "X"
                break
            else:
                print("Position already taken!")
        except:
            print("Invalid input!")

# Game loop
def play_game():
    print("🎮 Tic-Tac-Toe (You = X, AI = O)")
    print_board()

    while True:
        human_move()
        print_board()

        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

        print("🤖 AI is thinking...")
        ai_move()
        print_board()

        if check_winner(board, "O"):
            print("🤖 AI wins!")
            break
        if is_draw(board):
            print("🤝 It's a draw!")
            break

# Run game
if __name__ == "__main__":
    play_game()
