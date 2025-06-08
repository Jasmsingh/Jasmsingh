import itertools

# Simple Tic Tac Toe game for two players on the command line

def print_board(board):
    for row in board:
        print(" | ".join(cell or " " for cell in row))
        print("-" * 9)

def check_winner(board):
    lines = board + list(map(list, zip(*board)))
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] and all(cell == line[0] for cell in line):
            return line[0]
    return None

def full(board):
    return all(all(cell for cell in row) for row in board)

def tic_tac_toe():
    board = [["" for _ in range(3)] for _ in range(3)]
    players = itertools.cycle(["X", "O"])
    while True:
        print_board(board)
        player = next(players)
        move = input(f"Player {player}, enter row and column (e.g., 1 2): ")
        try:
            r, c = map(int, move.split())
            if not (0 <= r < 3 and 0 <= c < 3) or board[r][c]:
                print("Invalid move. Try again.")
                players = itertools.cycle([player, next(players)])
                continue
            board[r][c] = player
        except (ValueError, IndexError):
            print("Invalid input. Use two numbers between 0 and 2.")
            players = itertools.cycle([player, next(players)])
            continue
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    tic_tac_toe()
