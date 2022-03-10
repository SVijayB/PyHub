def solveNQueen(board, col):
    if col >= len(board):
        return True
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQueen(board, col + 1):
                return True
            board[i][col] = 0
    return False


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i = i + 1
        j = j - 1
    return True


def Output(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("X", end=" ")
        print()


if __name__ == "__main__":
    n = 8
    board = [[0 for i in range(n)] for j in range(n)]
    count = 0
    if solveNQueen(board, 0):
        Output(board)
    else:
        print("Solution doesn not exist")
