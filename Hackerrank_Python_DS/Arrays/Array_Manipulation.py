#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# The main hassle in this problem is in the finding maximum value from the prefix sum array (called cumulative sum in statistics course). I tried to parse through the array while rewriting the prefixsum and then call the max(array) but that fails for big test cases,so just parse through it and keep track of max element.

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+2) # Creating an array of n+2 zeros(indexing starts from 1, and to avoid out of bounds, took an extra block of space)
    for a,b,k in queries:
        arr[a] += k
        arr[b+1] -= k
    
    max_num = temp = 0
    for ele in arr:
        temp += ele
        max_num = max(max_num, temp)
    
    return(max_num)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
