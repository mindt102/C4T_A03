'''
import math
def get_delta(a,b,c):
    delta = b*b - 4*a*c 
    return delta

def get_quadro(a,b,c):
    delta = get_delta(a,b,c)
    if delta < 0:
        return "No solution"
    elif delta == 0:
        root = -b/(2*a)
        return root
    else:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        return root1,root2 

# print(get_quadro(1,1,1))
# print(get_quadro(1,2,1))
# print(get_quadro(1,-3,2))


def get_f(point_1 = [],point_2 = []):
    x1 = point_1[0]
    y1 = point_1[1]
    x2 = point_2[0]
    y2 = point_2[1]
    if point_1 == point_2:
        return '2 diem trung nhau'
    elif x1 == x2:
        return 'a bang bao nhieu cung duoc','b khong ton tai'
    elif y1 == y2:
        return 0,y1
    else:
        a = (y1 - y2) / (x1 - x2)
        b = y1 - a * x1
        return a,b    

# print(get_f([0,0],[0,0]))
# print(get_f([0,0],[1,1]))
# print(get_f([0,1],[0,2]))
# print(get_f([0,1],[1,1]))

def get_distance(a ,b ,c,point = []):
    x = point[0]
    y = point[1]
    tu_so = abs(a*x + b*y + c)
    mau_so = math.sqrt(a*a + b*b)
    return tu_so / mau_so

# print(get_distance(0,1,-1,[0,0]))
'''

# Recursive (de quy)
def hanoi_tower_recursion (n):
    ''' algorithm to resolve hanoi_tower problem
        - n: number of disk
        - result = count number of disk movement to solve the problem'''
    if n == 1:
        result = 1
    else:
        result = 2 * hanoi_tower_recursion(n-1) + 1
    return result

# print(hanoi_tower_recursion(5))


def find_minimum(list_n = []):
    if len(list_n) == 0:
        result = "Khong the dien list rong"
    elif len(list_n) == 1:
        result = list_n[0]
    else :
        if (list_n[0] >= list_n[-1]):
            result = find_minimum(list_n[1:])
        else:
            result = find_minimum(list_n[:-1])   
    
    return result


print(find_minimum([]))
