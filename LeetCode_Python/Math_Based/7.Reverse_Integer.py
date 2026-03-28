# https://leetcode.com/problems/reverse-integer/description/?envType=problem-list-v2&envId=math

class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        MIN_INT = -2**31
        MAX_INT = (2**31 - 1)

        sign = -1 if x < 0 else 1
        # Reverse the absolute value using string slicing
        reversed_val = int(str(abs(x))[::-1])

        # Apply the sign
        res = sign * reversed_val

        if(res < MIN_INT or res > MAX_INT):
            return 0
        return res