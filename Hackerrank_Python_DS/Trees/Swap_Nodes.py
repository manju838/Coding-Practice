#!/bin/python3

import math
import os
import random
import re
import sys
# Imports by me
from collections import deque
sys.setrecursionlimit(10000) # In constraints, 1 <= n<= 1024 while python's default recursionlimit is around 1000

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#
class Node:
    # Defining a tree constructor which has a root value, left and right nodes
    def __init__(self, val):
        self.info = val
        self.left = None
        self.right = None
        
def swapNodes(indexes, queries):
    # print(indexes)[[2, 3], [-1, -1], [-1, -1]]
    #print(queries) [1, 1]
    # Write your code here
    
    # Root node is 1
    root = Node(1)
    
    def create(root, indexes):
        # For DFS/recursion we use stack, for BFS we use queue
        q = deque([root]) # append,appendleft, pop, popleft are common functions
        for x,y in indexes:
            temp = q.popleft() # I need to build a tree so the root pointer is the final returnable 
            if x != -1: # If val is -1, then node doesn't exist according to question
                # Left node
                temp.left = Node(x)
                q.append(temp.left)
            if y != -1:
                # Right node
                temp.right = Node(y)
                q.append(temp.right)
        return root
    
    # Add nodes based on a BFS approach as mentioned in question
    root = create(root, indexes) # This fn must have the root node and the indexes list given in question
    
    def swap(root, level, k, temp_list):
        # If root exists
        if root:
            # Check if swap condition satisfies
            if level%k == 0:
                # Swap the nodes, no need to check if None/not as if None, it is just getting assigned to other side with no errors (in Python only)
                root.left, root.right = root.right, root.left
                
            # Once swap is performed, do inorder traversal according to problem
            # Visit left subtree
            swap(root.left, level+1, k, temp_list)
            # visit central node
            temp_list.append(root.info)
            # Visit right subtree
            swap(root.right, level+1, k, temp_list)
                
                
    
    
    result = []
    for k in queries:
        temp_list = []
        swap(root,1,k,temp_list) # For each query, we need to swap the nodes at that level and then do print the inorder traversal,so we need a temporary list which resets after each query
        result.append(temp_list)
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
