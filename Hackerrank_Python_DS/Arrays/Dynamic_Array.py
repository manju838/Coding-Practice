#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for i in range(n)] # Declaring 2D array of n empty arrays
    lastAnswer = 0
    ans = []
    for i, x, y in queries:
        idx = ((x^lastAnswer)%n) 
        if(i == 1):
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y%len(arr[idx])]
            ans.append(lastAnswer)

    # XOR is exclusive OR, so if there is only 1 exclusive 1 then it remains 1 else 0, so (1,0) and (0,    1) are 1; (0,0) and (1,1) are 0. Take 3 (0b 011),5 (0b 101) then XOR is 0b110 i.e 6
    return ans
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
