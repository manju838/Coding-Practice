# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# In this problem, we need to keep track of both linked lists as well as the carry as in the edge case, the 
# linked lists may have ended but the carry remains(like 8+7 = 15, there's no digits in ten's palce)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        cur_ptr = new_node
        carry = 0

        while(l1 or l2 or carry):
            #while(l1 != None or l2 != None or carry != 0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # write new digit(digits of sum)
            val = v1 + v2 + carry
            carry = val //10 # Always first extract the left digit and then only extract the right digit
            val = val % 10
            cur_ptr.next = ListNode(val)

            # Update pointers
            cur_ptr = cur_ptr.next
            l1 = l1.next if l1 else None # li is updated to l1.next only if array is present, so if l1 is True only if linked list is present
            l2 = l2.next if l2 else None
        
        return(new_node.next) # In hackerrank DS/Linked-List section questions, head given is not the node  but the node ptr so, we directly return it, here since we are creating a node, we need to give its pointer using .next

            
