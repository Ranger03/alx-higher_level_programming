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
    board = [['.' for _ in range(N)] for _ in range(N)]
    
    def backtrack(col):

        if col >= N:
            print_solution(board)
            return
        
        for row in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 'Q'
                backtrack(col + 1)
                board[row][col] = '.'
    
    def print_solution(board):
        for row in board:
            print(' '.join(row))
        print()
    
    backtrack(0)

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


solve_nqueens(N)

