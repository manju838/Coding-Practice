# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"This problem has a recursion variant which I didn't implement yet, check the official soln on leetcode"
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        O(n) time and O(n) space complexity
        
        nums = []

        while(head):
            nums.append(head.val)
            head = head.next
        
        left_ptr, right_ptr = 0, len(nums) - 1
        while(left_ptr <= right_ptr):
            if nums[left_ptr] != nums[right_ptr]:
                return False
            left_ptr += 1
            right_ptr -= 1
        return True
        '''
        '''
        We are using pointers to use only O(1) space complexity. For palindromes, from the middle it will be mirror images so if we have a pointer roughly at the middle and then check the values by pointers in opposite directions, we can confirm if its a palindrome or not

        Fast pointer parses twice the speed of the slow pointer so that by the time slow pointer reaches middle fast pointer reaches end
        Once the middle is figured out reverse the second part of the linked list so that the tail is at the middle of the linked list.
        Finally one pointer from left, one from right will parse and confirm if palindrome or not
        '''
        fast_ptr = head
        slow_ptr = head

        while fast_ptr and fast_ptr.next: # Loop until fast_ptr reaches end(None) or fast_ptr reached penultimate node
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        prev_ptr = None
        while slow_ptr:
            temp = slow_ptr.next
            slow_ptr.next = prev_ptr
            prev_ptr = slow_ptr
            slow_ptr = temp
        
        left_ptr,right_ptr = head, prev_ptr
        while right_ptr:
            if left_ptr.val != right_ptr.val:
                return False
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next
        return True


        
