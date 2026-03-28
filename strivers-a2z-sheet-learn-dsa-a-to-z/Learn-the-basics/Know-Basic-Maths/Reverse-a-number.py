# https://takeuforward.org/plus/dsa/problems/reverse-a-number?source=strivers-a2z-dsa-track


# Brute Force Approach[O(N) space complexity, type conversion overhead]:

"""
Time Complexity: O(log10(N))
    - abs(N): O(1)
    - str(abs(N)): O(log10(N)), log(N) base 10
    - [::-1] (reversing the string): O(log10(N))
    - int(...): Converting a string back into an integer involves iterating through each character of the string and performing math to build the number. This again takes O(log10(N)).
    Total = O(log10(N) + log10(N) + log10(N) + 1) => O(log10(N))

Space Complexity: O(N)
"""

class Solution:
    def reverseNumber(self, n):
        # Handle the sign separately
        sign = -1 if n < 0 else 1
        # Convert absolute value to string, reverse it, convert back to int
        reversed_num = int(str(abs(n))[::-1])
        # Reapply the original sign
        return sign * reversed_num

# Optimal Approach[O(log10(N)) time complexity, O(1) space complexity]:
class Solution:
    def reverseNumber(self, n):
        reverseNumber = 0
        while(n>0):
            lastDigit = n%10
            reverseNumber = reverseNumber*10+lastDigit
            n = n//10
        return(reverseNumber)