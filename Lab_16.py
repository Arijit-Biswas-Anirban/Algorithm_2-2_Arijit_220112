# Lab 16: N-Queen Problem, using backtracking

n = int(input("Enter number of queens: "))
board = [[0 for _ in range(n)] for __ in range(n)]
queen_positions = []

def check_column(board, row, column):
    for i in range(row, -1, -1):
        if board[i][column] == 1:
            return False
    return True

def check_diagonal(board, row, column):
    # secondary diagonal
    for i,j in zip(range(row,-1,-1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    # primary diagonal
    for i,j in zip(range(row,-1,-1), range(column, n, 1)):
        if board[i][j] == 1:
            return False
    return True

def placing_queens(board, row):
    if row == n:
        return True
    for col in range(n):
        if check_column(board, row, col) and check_diagonal(board, row, col):
            queen_positions.append(col+1)
            board[row][col] = 1
            if placing_queens(board, row+1):
                return True
            queen_positions.pop()
            board[row][col] = 0
    return False

def main():
    placing_queens(board, 0)
    
    for row in board:
        print(row)
    print(queen_positions)
main()