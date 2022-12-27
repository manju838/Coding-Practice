class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''
        Playing with Binary representation
        For a number to be a power of 2, in its binary representation, only one digit must be 1
        So subtract 1 from it and do an AND operation, if the result is 0 and n > 0(since subtraction is performed n must not be negative) then n is power of 2
        
        return(n > 0 and (n & (n-1)) == 0)
        '''

        #####################################
        '''
        In the constraints of the problem, -2^31 <= n <= 2^31 - 1, so use this to advantage

        (1<<31) means shifting bits of number 1 by 31 places. Shifting a binary digit means powering it with 2, (01 << 1) = 10, i.e 01* 2^1. If 2^2 = 4 and 2^3 = 8, then 8%4 = 0, i.e the max. no. formed by the constraint 2^31-1 must be divisible by 2^1

        Only a power of 2 will be able to divide a larger power of 2. Thus, we can take the largest power of 2 for our given range and check if n divides it

        return n > 0 and (1 << 31) % n == 0  
        '''
        #####################################

        '''
        ----> Recursive Implementation <----
        The no. can be divided by 2 and the edge cases are divident being even, the base case is 2^0 = 1 and n must be positive non zero no.
        
        if(not n): # If n == 0, not n is True
            return False
        if(n == 1): # Base case
            return True
        return(n%2 == 0 and self.isPowerOfTwo(n/2))
        '''

        '''
        ----> Iterative Implementation <----
        
        if(n == 0):
            return False
        while (n%2 == 0):
            n = n/2
        return n==1
        '''
        
        '''
        If the epxponent of 2 is perfect then log2(n) and trunc(log2(n)) must be same.
        trunc(3.5) = 3, trunc(-3.5) = -3

        return n > 0 and log2(n) == trunc(log2(n))
        '''

        '''
        As discussed in binary, only one 1 must be present in binary expression
        return n > 0 and bin(n).count('1') == 1

        '''

