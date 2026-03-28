# https://leetcode.com/problems/add-two-numbers/description/?envType=problem-list-v2&envId=math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
Nos. are stored in reverse(i.e 1st element is ones place, 2nd is tens place and so on.)
The sum is also stored in reverse, so add digits from 1st place to last and add carry values.
We create a linked list node with dummy value(0 here), keep looping until both the lists are traversed and adding values, the carry is stored and the last digit of addition is added as next element and finally, we return not the head(which is dummy value 0, but its next node)

Time complexity is O(max(m,n)) where m and n are the lengths of the two linked lists. Space complexity is also O(max(m,n)) for the new linked list created.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create the returning linked list and initialise a pointer
        res_ptr = ListNode(0) # Pointer for linked list created
        res_linked_list = res_ptr
        
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            added_val = val1+val2+carry
            carry = added_val//10
            new_digit = added_val%10

            res_linked_list.next = ListNode(new_digit)
            res_linked_list = res_linked_list.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return res_ptr.next

# Note: This code has multiple if conditional checks, once for getting val1, val2 and then again for moving the pointers of l1 and l2. We can reduce the number of if checks by using a single if check for l1 and l2 and then getting the values and moving the pointers in the same if block. This will reduce the number of if checks and make the code more efficient/faster in leetcode as shown below:

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        arr = dummy_head
        carry = 0

        # Explicitly using "is not None" makes the if comparison faster
        while l1 is not None or l2 is not None or carry:
            sub_sum = carry
            if l1:
                sub_sum += l1.val
                l1 = l1.next
            if l2:
                sub_sum += l2.val
                l2 = l2.next
            carry = sub_sum//10
            new_digit = sub_sum%10
            
            arr.next = ListNode(new_digit)
            arr = arr.next
        
        return dummy_head.next