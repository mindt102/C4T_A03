board_size = 1
board = []
for i in range(board_size):
    board.append([])
    for j in range(board_size):
        board[i].append(0)

def print_board(board):
    for row in board:
        for col in row:
            print(col,end=" ")
        print()
    print()
    return

def solve(board):
    if solve_recursion(board,0):
        print_board(board)
        return "Solved" 
    else:
        return "No solution"
def solve_recursion(board,row):
    if row == board_size:
        return True
    for col in range(board_size):
        if valid([row,col],board):
            board[row][col] = 1
            if solve_recursion(board,row+1):
                return True
        board[row][col] = 0
    return False
def valid(position,board):
    r, c = position
    for row in board:
        if row[c] == 1:
            return False
    dr = [1,1,-1,-1]
    dc = [1,-1,1,-1]
    for i in range(4):
        new_r = r + dr[i]
        new_c = c + dc[i]
        while 0 <= new_r < board_size and 0 <= new_c < board_size:
            if board[new_r][new_c] == 1:
                return False
            new_r += dr[i]
            new_c += dc[i]
    return True

print_board(board)
print(solve(board))

