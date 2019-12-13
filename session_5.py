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

def solve (bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(bo,i,[row,col]):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False

def find_empty(bo):
    for i in range (9):
        for j in range(9):
            if bo[i][j] == 0:
                return i,j
    return None

def valid(bo,num,pos):
    num_row,num_col = pos
    if num in bo[num_row]:
        return False
    if num in [bo[i][num_col] for i in range(9)]:
        return False
    box_col = (num_col//3)*3
    box_row = (num_row//3)*3
    if num in [ bo[i][j] for i in range(box_row,box_row+3) 
                         for j in range(box_col,box_col+3)]:
        return False
    return True
print_board(board)
print(solve(board))

print_board(board)