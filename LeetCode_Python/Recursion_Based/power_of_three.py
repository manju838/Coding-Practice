class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        '''
        ----> Iterative Solution <----
        if n < 1:
            return False
        while(n%3 == 0):
            n /= 3
        return(n == 1)
        '''

        '''
        ----> Recursive Solution <----
        Base case for a recursive usually involves both <1 and 1 together. As recursion in this case divides the number, it becomes smaller and smaller, so any result <1 are invalid and 1 is the base case for a power or multiplication like 0 for addition operation
        
        # Base case
        if(n<= 1):
            return(n == 1) # Returning False for n<1 (if condition) and True for n ==1 (elif condition) is a hassle so do it this way
        return(n%3 == 0 and self.isPowerOfThree(n/3))
        '''

        '''
        Base Conversion: Converting to base 3 format(like binary corresponds to 2^0,2^1.., base 3 is 3^0,3^1)
        for any power of k, in the base k; the leading digit will be 1 followed by 0s
        '''
 
        
