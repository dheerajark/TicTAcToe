def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[col][row] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    # return False


def is_board_full(board):
    if all([cell != " " for row in board for cell in row]):
        return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row = int(input(f"player {players[turn % 2]}, enter row(0-2)"))
        col = int(input(f"player {players[turn % 2]}, enter col(0-2)"))

        if board[row][col] != " ":
            print("That position is already taken")
            continue

        if board[row][col] == " ":
            board[row][col] = players[turn % 2]

        if check_winner(board, players[turn % 2]):
            print_board(board)
            print(f"player {players[turn % 2]}, wins.")
            break

        if is_board_full(board):
            print_board(board)
            print("This is a tie")
            break

        turn += 1


if __name__ == "__main__":
    main()
