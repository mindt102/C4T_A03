
def cavityMap(grid):
    n = len(grid)
    for i in range(1,n-1):
        for j in range(1,n-1):
            pos     = grid[i][j]
            # print("pos:",pos)
            up      = grid[i-1][j]
            down    = grid[i+1][j]
            left    = grid[i][j-1]
            right   = grid[i][j+1]
            if pos > max(up,down,left,right):
                grid[i] = grid[i][:j] + "X" + grid[i][j+1:]
                print("pos: ",i,j,pos)
                print("up:",up,"down:",down,"left:",left,"right:",right)
    return grid

grid = [
    '123456',
    '234672',
    '235268',
    '635648',
    '465524',
    '893456',
]

def print_grid(grid):
    for row in grid:
        print(row)
    print()
print_grid(grid)
print_grid(cavityMap(grid))