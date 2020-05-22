''' Câu 1 '''
def sum_Numb(numb):
    if numb < 10:
        return numb
    else:
        return numb%10 + sum_Numb(numb // 10)

''' Câu 2 '''
def sum_n_number(n):
    if n == 1:
        return 1
    else:
        return n + sum_n_number(n-1)
    
''' Câu 3 '''
def convert_to_binary(n):
    result = 0
    i = 0
    while n != 0:
        result += (n % 2)*pow(10,i)
        n = n // 2
        i += 1
    return result

print(convert_to_binary(17))

''' Câu 4 '''
def maze_runner(maze): # Main function
    maze[0][0] = 2
    if Solve_maze(maze,[0,0]):
        print_maze(maze)
        return "Solved"
    else:
        return "Can't solve"

def Solve_maze(maze,position): # Recursion function
    x,y = position
    if x == y and x == len(maze) - 1:
        return True
    next_move = find_next_move(maze,position)
    for move in next_move:
        next_x , next_y = move
        current_value = maze[next_x][next_y] 
        maze[next_x][next_y] = 2
        if Solve_maze(maze,move):
            return True
        maze[next_x][next_y] = current_value
    return False

def find_next_move(maze, position):
    side_length = len(maze)
    valid_move = []
    x,y = position
    dx = [1,-1, 0, 0]
    dy = [0, 0, 1,-1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < side_length and 0 <= new_y < side_length and maze[new_x][new_y] == 1:
            valid_move.append([new_x,new_y])
    return valid_move
maze = [ [1, 0, 1, 1, 1], 
         [1, 0, 1, 0, 1], 
         [1, 0, 1, 0, 1], 
         [1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1,] ]

def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze)):
            print(maze[i][j],end = " ")
        print()
    print()

# print_maze(maze)
# print(maze_runner(maze))

''' Câu 5 '''
def possible_journey(start, destination):
    sx, sy = start
    dx, dy = destination
    if sx == dx and sy == dy:
        return True
    if sx*sy > 0 and (abs(sx) > abs(dx) or abs(sy) > abs(dy)):
        return False
    if sx == sy and sx == 0:
        return False
    if sx == 0:
        return possible_journey([sx + sy, sy],[dx,dy])
    if sy == 0:
        return possible_journey([sx, sx + sy],[dx,dy])
    return possible_journey([sx + sy, sy],[dx,dy]) or possible_journey([sx, sx + sy],[dx,dy])

# print(possible_journey([-5,9],[11,4]))
''' Câu 6 '''
import math

def square_sum(x,n):
    ways = 0
    for i in range(1,x+1):
        if pow(i,n) > x:
            return ways
        ways += square_sum_recursion(x - pow(i,n), n, i+1) 
    return ways

def square_sum_recursion(x,n,start):
    if x == 0:
        return 1
    ways = 0
    for i in range(start,x+1):
        if pow(i,n) > x:
            return ways
        ways += square_sum_recursion(x - pow(i,n), n,i+1)
    return ways

# for i in range(100):
#     ways = square_sum(i,2) 
#     if  ways > 3:
#         print("Number: {}, ways: {}".format(i,ways)) 

''' Câu 7 '''
def find_min_move(n):   # Main function
    if n == 0:              
        return 0
    n = abs(n)                  
    largest_min_move = find_min_move(n-1) + 2
    return find_min_move_recursion(n, 0, 1, largest_min_move)
    
def find_min_move_recursion(n, position, step, largest_min_move):
    if position == n:
        return step - 1
    if step >= largest_min_move:
        return largest_min_move
    else:
        return min( find_min_move_recursion(n, position + step, step + 1, largest_min_move), find_min_move_recursion(n, position - step, step + 1,largest_min_move) )

# for i in range(1,21):
i = 12
print("{}. move: {}".format(i,find_min_move(i)))

