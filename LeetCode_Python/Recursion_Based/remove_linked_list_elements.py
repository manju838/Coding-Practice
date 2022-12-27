# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # cur_ptr = head, ---> Never Initialise this way, it works for hackerrank due to its constructor class but leetcode follows (data, addr) type of representation with no default data value, so it just fails <---
        '''
        print(cur_ptr)
        Output: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 6, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}}

        print(cur_ptr.val)
        Output: 1

        print(cur_ptr.next)
        Output: ListNode{val: 2, next: ListNode{val: 6, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 6, next: None}}}}}}
        '''
        dummy = ListNode(0)
        print(dummy)
        dummy.next = head
        cur,prev = head, dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        
        return(dummy.next)

        
        
