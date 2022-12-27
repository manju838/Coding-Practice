# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Since we need to parse through two linked lists whose sizes are not known, for loop is not efficient
# While loop may work but we need to check which linked list terminates first and we get 3 conditions, l1< l2, l1 > l2, l1 = l2. So we need to write, while(l1.next != None and l2.next == None) for case 1 similarly for case 2 and for case 3 while(l1.next == None and l2.next == None).

# To avoid a lot of explicit conditions and complexity, we define when the comparision needs to be terminated and what to do if the comparison is terminated(one of the list is completed) using 
# --> Recursion <--

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Writing base cases
        # Both lists were empty
        if(l1 == None and l2 == None):
            return(None)
        # If only list1 is empty
        if(l1 == None):
            return(l2)
        # If only list2 is empty
        if(l2 == None):
            return(l1)
        
        temp = dummy = ListNode(0) # This is a dummy node and as the constructor doesn't hve a default value, we initialised it to 0
        while(l1 and l2):
            if(l1.val < l2.val):
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next # If this is not written, the output would be a single element linked list
        if(l1):
            temp.next = l1
        if(l2):
            temp.next = l2
        return(dummy.next)

