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

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#


# Since we need to parse through two linked lists whose sizes are not known, for loop is not efficient
# While loop may work but we need to check which linked list terminates first and we get 3 conditions, l1< l2, l1 > l2, l1 = l2. So we need to write, while(l1.next != None and l2.next == None) for case 1 similarly for case 2 and for case 3 while(l1.next == None and l2.next == None).

# To avoid a lot of explicit conditions and complexity, we define when the comparision needs to be terminated and what to do if the comparison is terminated(one of the list is completed) using 
# --> Recursion <--

# Possible Debugging:
# Wrong Answer: Didn't initialise properly; Used head.next instead of head; return statement has some indentation issue(like returning inside a loop/condition instead of outer loop)
# Runtime Error: Code is complex with a lot of new variables and write statements(check if the answer is to check for a single variable like max or return the entire array); sys.setrecursionlimit(high value)

import sys
sys.setrecursionlimit(100000)

def mergeLists(head1, head2):
    #Extreme Cases
    # Both lists are empty
    if(head1 == None and head2 == None):
        return(None)
    # Head1 is empty
    if(head1 == None):
        return(head2)
    # Head2 is empty
    if(head2 == None):
        return(head1)
    
    temp = None
    if(head1.data < head2.data):
        temp = head1
        temp.next = mergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists(head1,head2.next)
    
    return(temp)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)
            
        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)

        print_singly_linked_list(llist3, ' ', fptr)
        fptr.write('\n')

    fptr.close()
