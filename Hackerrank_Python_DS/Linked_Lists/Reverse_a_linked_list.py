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
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

# The logic here is to take 3 ptrs, prev_ptr will be None initially, cur_ptr will be head/llist and nxt_ptr will be head.next/llist.next
# We first mark the next ptr then we change the link b/w cur_ptr and prev_ptr, mark prev_ptr as cur_ptr and mark cur_ptr as nxt_ptr and repeat the same logic.  

def reverse(llist):
    # Write your code here
    prev_ptr = None
    cur_ptr = llist
    nxt_ptr = llist.next
    
    while(cur_ptr !=None):
        nxt_ptr = cur_ptr.next
        cur_ptr.next = prev_ptr # This reverses the link so marking the next node comes first
        prev_ptr = cur_ptr # Once link is reversed, marking previous node is not needed so shift it to current node
        cur_ptr = nxt_ptr # Once previous is shifted, current needs to move on
    llist = prev_ptr
    
    return(llist)
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = reverse(llist.head)

        print_singly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
