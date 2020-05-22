def Create_board(n):
    board = []
    '''Create a board with 0 as empty spaces'''
    for i in range(n):
        board.append([])
        for j in range(n):
            board[i].append(0)
    return board

def Print_board(board):
    '''Print the board'''
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()
    print()
def valid_move(move):
    row, col = move
    for r in range(len(board)):
        if board[r][col] == 1:
            # print("\tSame col: ",(r, col))
            return False
    dr = [1, 1, -1, -1]
    dc = [1, -1, 1, -1]
    for i in range(4):
        row, col = move
        while 0 <= row + dr[i] and row + dr[i]  < len(board) and 0 <= col + dc[i] and col + dc[i] < len(board):
            row += dr[i]
            col += dc[i]
            if board[row][col] == 1:
                # print("\tSame diag: ",(row, col))
                return False
    return True

solutions = 0
def Queens_maker(board, queens_numb):
    if queens_numb == len(board):
        Print_board(board)
        global solutions
        solutions += 1
    else:
        for col in range(len(board)):
            # print("Queens_numb, col: ({},{})".format(queens_numb, col))
            if valid_move((queens_numb, col)):
                board[queens_numb][col] = 1
                Queens_maker(board, queens_numb + 1)
                board[queens_numb][col] = 0

# board = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
# ]

n = int(input("Enter n: "))
board = Create_board(n)
Print_board(board)
Queens_maker(board, 0)
if solutions == 0:
    print("No solution")
else:
    print("Total {} solution(s)".format(solutions))
