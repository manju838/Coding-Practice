#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

'''
Let positionFromTail = x and total length of linked list = n

|----(n-x) elements ----|----x elements----|
First traverse a temporary pointer to x elements
|----x elements ----|----(n-x) elements----|
Noe move both pointers while the first pointer reaches end, second traverses (n-x) elements. Then it is n elements away from the end of linked list

'''

def getNode(llist, positionFromTail):
    # print(llist)
    ptr_1 = llist
    ptr_2 = llist
    
    for i in range(positionFromTail):
        ptr_1 = ptr_1.next
    
    while(ptr_1.next != None):
        ptr_1 = ptr_1.next
        ptr_2 = ptr_2.next
    
    return(ptr_2.data)
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = getNode(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()
