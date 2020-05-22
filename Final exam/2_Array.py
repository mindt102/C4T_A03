LENGTH = 7

arr = []
for i in range(7):
    element = input("Enter a number: ")
    while not element.isdigit():
        print("Invalid")
        element = input("Enter a number: ")
    arr.append(int(element))
print("Array: {}".format(arr))
print("Sum: {}".format(sum(arr)))
print("Max: {}".format(max(arr)))
print("Min: {}".format(min(arr)))
x = input("Enter x: ")
if not x.isdigit():
    print("{} appears 0 time(s) in the array".format(x))
else:
    x = int(x)
    print("{} appears {} time(s) in the array".format(x, arr.count(x)))