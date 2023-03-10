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

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

'''
Given:
"The merge point is where both lists point to the same node, i.e. they reference the same memory location"

There is a handicap in this problem that both the lists are different and both are not empty(given not NULL)

For lists with different lengths, finding difference and traversing that difference for the longest linked list will assure that the difference is mostly the common part of both the linked lists.

Even if it is not the case just take the nodes after taking difference as the base case and parse through both the lists with pointer increments
'''
def findMergeNode(head1, head2):
    
    # Define a fn to count no.of elements of linked list
    def getCount(head):
        count = 0
        while(head.next != None):
            count +=1
            head = head.next
        return count
    
    # Count the length of linked lists
    c1 = getCount(head1)
    c2 = getCount(head2)
    
    # Get the common Node
    def getnode(d, head1, head2):
        # Traverse Upto d in first linked list
        for i in range(d):
            head1 = head1.next
        
        # Check for common node
        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next
    
    # Check the difference
    if c1 > c2:
        return getnode(c1 - c2, head1, head2)
    else:
        return getnode(c2 - c1, head2, head1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

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
            
        ptr1 = llist1.head;
        ptr2 = llist2.head;

        for i in range(llist1_count):
            if i < index:
                ptr1 = ptr1.next
                
        for i in range(llist2_count):
            if i != llist2_count-1:
                ptr2 = ptr2.next

        ptr2.next = ptr1

        result = findMergeNode(llist1.head, llist2.head)

        fptr.write(str(result) + '\n')

    fptr.close()