#!/usr/bin/python3

"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys

def is_safe(board, row, col, N):
    # Check if the current position is safe from attacks
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    return True

def solve_nqueens(N):
    # Initialize an empty board
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    def backtrack(col):
        # Base case: all queens are placed
        if col >= N:
            print_solution(board)
            return
        
        # Try placing the queen in each row of the current column
        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'
    
    def print_solution(board):
        # Print the board configuration
        for row in board:
            print(' '.join(row))
        print()
    
    # Start the backtracking algorithm
    backtrack(0)

# Check the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the N queens problem
solve_nqueens(N)

