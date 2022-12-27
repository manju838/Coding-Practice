class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        '''
        Iterative Solution

        if(n < 1):
            return False
        while(n%4 == 0):
            n /=4
        return(n == 1)
        '''
        # Recursive Solution
        if(n <=1):
            return(n == 1)
        while(n%4 == 0):
            return(n > 0 and self.isPowerOfFour(n/4))


