loop = True
while loop:
    number = input("Enter your number: ")
    if number.isdigit():
        loop = False
        
print('The length of your number is {}'.format(len(number)))