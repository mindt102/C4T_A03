#!/bin/python3

import os
import sys

#
# Complete the bonetrousle function below.
#
def bonetrousle(n, k, b):
    #
    # Write your code here.
    #
    store_boxes = list(range(1,k+1))
    if sum(store_boxes[-k:]) < n or sum(store_boxes[:-k+1]) > n:
        return [-1]
    

t = int(input())

for t_itr in range(t):
    nkb = input().split()

    n = int(nkb[0])

    k = int(nkb[1])

    b = int(nkb[2])

    result = bonetrousle(n, k, b)

    print(' '.join(map(str, result)))
    print('\n')


