# https://leetcode.com/problems/palindrome-number/description/?envType=problem-list-v2&envId=math

# Solution 1: Without converting to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_num = 0
        original_num = x
        while(x>0):
            last_digit = x%10
            reverse_num = reverse_num*10 + last_digit
            x = x//10
        # print(x, reverse_num)
        if(original_num==reverse_num):
            return True
        else:
            return False

# Note1: If instead of while(x>0), we have if x<0: return False and then use while x:, our soln is the slowest on leetcode while just joining these 2 as above beats 90% of submissions.
# Disclaimer Note2: When we manipulate the number directly(x in the above case), checking if x==reverse_num at the end is not correct as x is 0 at the end of the loop, so we need to save the original value in a separate variable and check with that at the end.

# Solution 2: Convert to string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            # If negative value(-123), it's not palindrome(321-)
            return False
        # Save original value, typecast to string and reverse the value(not using abs() as we are not handling negatives)
        original_x = x
        reversed_x = int(str(x)[::-1])
        if(original_x == reversed_x):
            return True
        else:
            return False

# Old solution:
'''
For a palindrome, we need to check the right and left most digits, if same chop them off and recursively check or else return not palindrome.
To get right digit => %10
To get left digit => // divisor (changes for each iteration)

Strategy: Set the initial divisor and then edit it for each loop
Eg: If num = 108, divisor = 100, if num = 10008, div = 1000
Start with divisor = 1, if num >= 10 times divisor, then update divisor as divisor = 10*divisor and continue this with a while loop to get the highest divisor value corresponding to the first unchopped number( also largest no.)
After each iteration, since two digits are chopped off, update divisor //100

To chop off  right digit => // 10
To chop off  left  digit => % divisor
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False

        divisor = 1
        while(x >= 10* divisor):
            divisor = 10 * divisor
        
        while x: # while x is True
            right_digit = x % 10
            left_digit = x // divisor

            if(left_digit != right_digit): return False

            x = (x % divisor) // 10
            divisor = divisor //100
        return True
