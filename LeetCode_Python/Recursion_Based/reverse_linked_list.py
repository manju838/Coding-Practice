# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
head => 1 -> 2 -> 3 ->4 -> None
newHead = 1

head => 2 -> 3 ->4 -> None
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        ----> Iterative Solution <----
                prev, cur = None, head
                while(cur):
                    temp_nxt_ptr = cur.next
                    cur.next = prev
                    prev = cur
                    cur = temp_nxt_ptr
                return(prev)

        '''

        '''
        ----> Recursive Solution <----
        '''
        # For last element, head == None so, not head is True only for the last element
        # For recursion define the base case so the last case will be the base case
        if not head: 
            return None
        
        newHead = head # This variable is used to propagate head for each of sub problems
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return(newHead)