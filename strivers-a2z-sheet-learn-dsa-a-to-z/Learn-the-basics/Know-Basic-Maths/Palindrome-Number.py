# https://takeuforward.org/plus/dsa/problems/palindrome-number?source=strivers-a2z-dsa-track

# Time Complexity: O(log10(N)+1)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, n):
        dupNum = n
        revNum = 0

        while(n>0):
            last_digit = n%10
            revNum = revNum*10+last_digit
            n = n//10
        
        if(dupNum == revNum):
            return(True)
        else:
            return(False)