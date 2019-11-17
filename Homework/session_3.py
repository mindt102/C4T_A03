def factorial(n = int):
    if n < 0:   
        return "Input an integer larger than 0"        
    elif n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def fibonaci(n):
    if n <= 0:
        return "Input an integer larger than 0"
    elif n == 1 :
        return 0
    elif n == 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

        
def pascal_triangle(n):
    if n <= 0:
        return "Input an integer larger than 0"
    elif n == 1:
        line = [1]
    else:
        line = []
        previous_line = pascal_triangle(n-1)
        for i in range(len(previous_line) - 1):
            line.append(previous_line[i] + previous_line[i+1])
        line = [1] + line + [1]
    return line

