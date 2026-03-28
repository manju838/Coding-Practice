# https://takeuforward.org/plus/dsa/problems/count-all-digits-of-a-number?source=strivers-a2z-dsa-track


# Brute Force Approach[O(log10(N)) time complexity]:
"""
Mathematically, the number of times you can divide a number N by a base B before it reaches 1 is floor[logB(N)].(floor of log N to the base B)
So, O(log10(N) + 1) => O(log10(N))

"""
# Math formula: [./image1.png]
class Solution:
    def countDigit(self, n):
        digit_counter = 0
        while(n > 0):
            digit_counter+=1
            # Remove last digit(modulo 10) and update n 
            n = n//10
        # The above loop runs till one digit is left, so add another 1 to counter
        digit_counter+=1
        return(digit_counter)

# Optimal Approach[O(1) time complexity]:
class Solution:
    def countDigit(self, n):
        import math
        digit_counter = int(math.log10(n) + 1)
        return(digit_counter)