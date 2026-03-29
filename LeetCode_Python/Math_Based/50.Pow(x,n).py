# https://leetcode.com/problems/powx-n/description/?envType=problem-list-v2&envId=math

'''
For x^8, instead of multiplying 8 times, we can write it as:
x^8 = (x^4)^2
x^4 = (x^2)^2
x^2 = (x^1)^2
By squaring the base and halving the exponent, we reach the answer in just 3 steps instead of 8. This changes the time complexity from O(n) to O(logn).

Say, for 2^9
res = 1
x = 2
n = 9
if n is odd(9 here): res *= x
x = x*x
'''

# Iterative Method:
class Solution:
    def myPow(self, x: float, n: int) -> float:
            if(n < 0):
                x = 1/x
                n = -n
            
            res = 1
            while(n>0):
                if(n%2==1):
                    res *=x
                
                # Double the base and half the exponent(use // operator to do integer division so that we dont handle odd case seperately)
                x*=x
                n = n//2
            return res