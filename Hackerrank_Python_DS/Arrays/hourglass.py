#!/bin/python3

import math
import os
import random
import re
import sys

#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

# Complete the 'hourglassSum' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# When using variables in python, initialise all of them orelse some variable (like partial_sum) may disturb another variable(like max_sum) and give assignment before definition error 

def hourglassSum(arr):
    max_sum = -50000
    partial_sum = 0
    # Write your code here
    
    for row in range(4):
        for col in range(4):
            # print(math_sum)
            partial_sum = arr[row][col] + arr[row][col+1] + arr[row][col+2] + arr[row+1][col+1] + \
            arr[row+2][col] + arr[row+2][col+1] + arr[row+2][col+2]
            #print(partial_sum)--> Clear till here
            max_sum = max(max_sum, partial_sum)
            # print(math_sum)

    return(max_sum) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
