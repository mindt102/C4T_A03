loop = True
while loop:
    n = input("Enter a number: ")
    if not n.isdigit:
        continue
    n = int(n)
    if n < 0:
        continue
    loop = False

factorial = 1
for i in range (1,n+1):
    factorial *= i
print("{}! is {}" .format(n,factorial))
