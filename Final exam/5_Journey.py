def create_board(input_string):
    board = []
    for i in range(len(input_string)):
        board.append([])
        for j in range(i, len(input_string)):
            board[i].append(input_string[j])
    return board

def print_board(board):
    for line in board:
        for char in line:
            print(char, end=" ")
        print()

def find_moves(board, char, position):
    row, col = position
    moves = []
    if col + 1 < len(board[row]):
        if board[row][col + 1] == char:
            moves.append((row, col + 1))
    if col - 1 >= 0:
        if board[row][col - 1] == char:
            moves.append((row, col - 1))
    if row + 1 < len(board):
        if board[row + 1][col] == char:
            moves.append((row + 1, col))
    if row - 1 >= 0:
        if board[row - 1][col] == char:
            moves.append((row - 1, col))
    return moves

counter = 0
def find_journey(board, input_string, position, char_numb):
    if char_numb + 1 == len(input_string):
        global counter
        counter += 1
        row, col = position
        board[row][col] = "*"
        print_board(board)
        board[row][col] = input_string[char_numb]
        print("Number {}".format(counter))
    else:
        row, col = position
        board[row][col] = "*"
        moves = find_moves(board, input_string[char_numb + 1], position)
        for move in moves:
            find_journey(board, input_string, move, char_numb + 1)
        board[row][col] = input_string[char_numb]

input_string = input("Enter your string: ")
board = create_board(input_string)
print_board(board)
find_journey(board, input_string, (0,0), 0)
