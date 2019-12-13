n = 9

def print_solution(board):
    for i in range(n):
        for j in range(n):
            if len(str(board[i][j])) == 1:
                print("0" + str(board[i][j]),end = " ")    
            else:
                print(str(board[i][j]),end = " ")
        print()

def solveKT():
    board = [[-1 for _ in range(n)] for _ in range(n)]
    if Solve([0,0],0,board):
        print_solution(board)
    else:
        print("No solution")

def Solve(pos,step,board):
    row,col = pos
    board[row][col] = step
    if step == pow(n,2) - 1:
        return True
    moves = findMoves(row,col,board)
    if len(moves) == 0:
        return False
    # print(step)
    for move in moves:
        # time.sleep(1)
        # print_solution(board)
        # print()
        r,c = move
        board[r][c] = step+1
        if Solve(move,step+1,board):
            return True
        board[r][c] = -1
    return False

def findMoves(r,c,board):
    moves = []
    if 0 <= r-1:
        if 0 <= c-2 and board[r-1][c-2] == -1:
            moves.append([r-1,c-2])
        if n > c+2  and board[r-1][c+2] == -1:
            moves.append([r-1,c+2])
        if 0 <= r-2:
            if 0 <= c-1 and board[r-2][c-1] == -1:
                moves.append([r-2,c-1])
            if n > c+1  and board[r-2][c+1] == -1:
                moves.append([r-2,c+1])
    if n > r+1:
        if 0 <= c-2 and board[r+1][c-2] == -1:
            moves.append([r+1,c-2])
        if n > c+2  and board[r+1][c+2] == -1:
            moves.append([r+1,c+2])
        if  n > r+2:
            if 0 <= c-1 and board[r+2][c-1] == -1:
                moves.append([r+2,c-1])
            if n > c+1  and board[r+2][c+1] == -1:
                moves.append([r+2,c+1])
    return moves
    
solveKT()

