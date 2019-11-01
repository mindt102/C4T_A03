# Try Exception
'''
ex 1: handle ValueError
NOTE:
TODO:

loop = True
number = 10
while loop:
    x = input('Insert a number: ')
    try:
        n = int(x)
        print(number / n)
        loop = False
    except ValueError: # except Exception dùng cho mọi lỗi
        print('wrong input')
    except ZeroDivisionError:
        print("can't divide by zero")
'''
'''
# problem_2
from random import randint
input_lst = []

for i in range(10):
    input_lst.append(randint(1,10))
print(input_lst)

print("a.",end=" ")
print(input_lst[:3])

print("b.",end=" ")
print(input_lst[-3:])

print("c.",end=" ")
for i in range(len(input_lst)-1):
    for j in range(i+1,len(input_lst)):
        if (input_lst[i] > input_lst[j]):
            input_lst[i],input_lst[j] = input_lst[j],input_lst[i]
print(input_lst)

print("d.",end=" ")
for i in range(len(input_lst)-1):
    for j in range(i+1,len(input_lst)):
        if (input_lst[i] < input_lst[j]):
            input_lst[i],input_lst[j] = input_lst[j],input_lst[i]
print(input_lst)
'''

'''
# Selection sort
from random import randint
def randomList ():
    input_lst = []
    for i in range(10):
        input_lst.append(randint(1,10))
    return input_lst
selection_lst = randomList()

print("Selection sort:")
print(selection_lst)
for i in range(len(selection_lst)-1):
    lowest_index = i
    for j in range(i+1,len(selection_lst)):
        if (selection_lst[j] < selection_lst[lowest_index]):
            lowest_index = j
    selection_lst[i],selection_lst[lowest_index] = selection_lst[lowest_index],selection_lst[i] 

print(selection_lst)


# Bubble sort
print("Bubble sort:")
swapped = True
bubble_list = randomList()
print(bubble_list)
while swapped:
    swapped = False
    for i in range(len(bubble_list)-1):
        if bubble_list[i] > bubble_list[i+1]:
            bubble_list[i],bubble_list[i+1] = bubble_list[i+1],bubble_list[i]
            swapped = True
print(bubble_list)
'''

'''
NOTE: chang a key to other key
person['sex'] = person.pop('gender')
'''
import math
lst1 = [1,3,4,16,32,8,64,4,128,2,256,32]
lst2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]

NUMBER = 256
squareroot = math.sqrt(NUMBER)
square = False

position1 = {}
position2 = {}

if(NUMBER % squareroot == 0):
    square = True
    squareroot = int(squareroot)
    position1[str(squareroot)] = []
    position2[str(squareroot)] = []

print("List 1: {}".format(lst1))
for i,numb in enumerate(lst1):
    if square and numb == squareroot:
        position1[str(squareroot)].append(i)
    else:
        position1[str(numb)] = i
for k in position1:
    firstnumb = int(k)
    if firstnumb < squareroot and NUMBER % firstnumb == 0:
        secondnumb = NUMBER // firstnumb
        if str(secondnumb) in position1.keys():
            print('{} and {} in positions {} and {}'.format(firstnumb,secondnumb,position1[k],position1[str(secondnumb)]))
    elif firstnumb == squareroot and len(position1[k]) > 1:
        print('{} and {} in positions {} and {}'.format(firstnumb,firstnumb,position1[k][0],position1[k][0][1]))

print("List 2: {}".format(lst2))
for i,numb in enumerate(lst2):
    if square and numb == squareroot:
        position2[str(squareroot)].append(i)
    else:
        position2[str(numb)] = i
for k in position2:
    firstnumb = int(k)
    if firstnumb < squareroot and NUMBER % firstnumb == 0:
        secondnumb = NUMBER // firstnumb
        if str(secondnumb) in position2.keys():
            print('{} and {} in positions {} and {}'.format(firstnumb,secondnumb,position2[k],position2[str(secondnumb)]))
    elif firstnumb == squareroot and len(position2[k]) > 1:
        print('{} and {} in positions {} and {}'.format(firstnumb,firstnumb,position2[k][0],position2[k][1]))



'''
appeared1 = []
appeared2 = []
print("List 1")
print(lst1)
for i in range(len(lst1) - 1):
    numb = lst1[i]
    if 256 % numb == 0 and numb not in appeared1:
        pair = 256 // numb
        for j in range(i+1,len(lst1)):
            if lst1[j] == pair:
                appeared1.append(numb)
                appeared1.append(pair)
                print('{} and {} in positions {} and {}'.format(numb,pair,i,j))
print("List 2:")
print(lst2)
for i in range(len(lst2) - 1):
    numb = lst2[i]
    print(numb in appeared2)
    if 256 % numb == 0 and numb not in appeared2:
        pair = 256 // numb
        for j in range(i+1,len(lst2)):
            if lst2[j] == pair:
                appeared2.append(numb)
                appeared2.append(pair)
                print('{} and {} in positions {} and {}'.format(numb,pair,i,j))



'''