'''
high = 100
low = 1
while True:
    avg = (high+low)//2
    print("Is your number",avg)
    ans = input()
    if ans == "c":
        break
    elif ans == "l":
        low = avg
    elif ans == "s":
        high = avg
'''
######
'''
import random

secret_numb = random.randint(1,100)

print(secret_numb)
loop = True
while loop:
    ans = int(input("Enter number from 1 to 100: "))
    if ans == secret_numb:
        loop = False
        print('Correct')
    elif ans > secret_numb:
        print("Your number is too large")
    else:
        print("Your number is too small")
'''

'''
loop = True
while loop:
    number = input("Enter your number: ")
    if number.isdigit():
        loop = False
        
print('The length of your number is',len(number))
'''

'''
numb = int(input('Enter a number larger than one: '))

loop = True
even_numb = 2
while loop:
    print(even_numb,end=" ")
    even_numb += 2
    if even_numb > numb:
        loop = False
        print()

for i in range(2,numb+1,2):
    print(i,end=" ")
'''
#math_3
'''
numb = int(input('Enter a number larger than one: '))
numb -= numb%2
for i in range(numb,0,-2):
    print(i,end=" ")
'''

#math_4
from math import sqrt

numb = int(input('Enter a number: '))

def checkPrime(numb):
    if numb < 2:
        return False
    else:
        numb_sqrt = int(sqrt(numb))
        for i in range(2, numb_sqrt + 1):
            if (numb_sqrt % i == 0):
                return False
        return True

if checkPrime(numb):
    print('{} is a prime number'.format(numb))
else:
    print('{} is a not prime number'.format(numb))