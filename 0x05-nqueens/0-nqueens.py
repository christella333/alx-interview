#!/usr/bin/env python3
import sys

def print_usage_and_exit(message, status):
    """Prints an error message and exits with a given status."""
    print(message)
    sys.exit(status)

def is_safe(board, row, col, n):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, col, n, solutions):
    """Uses backtracking to find all solutions to the N Queens problem."""
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n, solutions)
            board[i][col] = 0

def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)
    if n < 4:
        print_usage_and_exit("N must be at least 4", 1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()

