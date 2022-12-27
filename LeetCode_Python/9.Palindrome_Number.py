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

