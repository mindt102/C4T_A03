def GCD(a, b):
    """Return the greatest common divisor of a and b"""
    if a == b:
        return a
    else:
        return GCD(max(a,b) - min(a,b), min(a,b))

def is_valid(n):
    """Return true if the number is an integer larger than 0"""
    if n.isdigit():
        n = int(n)
        if n > 0:
            return True
    return False

a = input("Enter the first number: ")
while not is_valid(a):
    print("Invalid number.")
    a = input("Enter the first number: ")
a = int(a)

b = input("Enter the second number: ")
while not is_valid(b):
    print("Invalid number.")
    b = input("Enter the second number: ")
b = int(b)

gcd = GCD(a, b)
print(a, b)
print("GCD: {}".format(gcd))
print("Minimalist fractions of {}/{}: {}/{}".format(a, b, a//gcd, b//gcd))
