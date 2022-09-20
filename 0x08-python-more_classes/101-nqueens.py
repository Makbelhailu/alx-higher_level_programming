#!/usr/bin/python3
"""solution for queens"""


def safe(board, row, col):
    """Checks if position is safe from attack."""

    for c in range(col):
        if board[c] is row or abs(board[c] - row) is abs(c - col):
            return False
        return True


def check(board, col):
    """Checks the board state column by column using backtracking."""

    n = len(board)
    if col is n:
        print(str([[c, board[c]] for c in range(n)]))
        return
    for row in range(n):
        if safe(board, row, col):
            board[col] = row
            check(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    i = 0
    try:
        i = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)
    if i < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(i)]
    check(board, 0)
