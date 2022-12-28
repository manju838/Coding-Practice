#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(llist, data):
    # Write your code here
    new_node = DoublyLinkedListNode(data)
    
    # If linked list is empty
    if(llist == None):
        llist = new_node
    
    # Insert node before head(starting of linked list)
    elif(data < llist.data):
        new_node.next = llist
        llist.prev = new_node
        llist = new_node
    
    # Inserting node somewhere in the middle of the linked list
    else:
        temp = llist
        while(temp.next != None and temp.data < data):
            temp = temp.next
        
        # If the insertion is at end of list(first part of while loop condition)
        if(temp.next == None and temp.data < data):
            temp.next = new_node
            new_node.prev = temp
        else:
            previous = temp.prev
            previous.next = new_node
            new_node.prev = previous
            
            new_node.next = temp
            temp.prev = new_node

    return llist
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sortedInsert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
