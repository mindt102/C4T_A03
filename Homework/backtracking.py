board = [  
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]   ]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def solve(board):
    empty_space = find_empty(board)
    if not empty_space:
        return True
    row,col = empty_space
    for i in range(1,9):
        if valid(i,row,col,board):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False     


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i,j]
    return None

def valid(value,row,col,board):
    if value in board[row]:
        return False
    if value in [board[i][col] for i in range(9)]:
        return False
    box_row = (row//3)*3
    box_col = (col//3)*3
    if value in [board[i][j] for i in range(box_row) for j in range(box_col)]:
        return False
    return True
solve(board)
print_board(board)