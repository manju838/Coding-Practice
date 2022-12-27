class Solution:
    def fib(self, n: int) -> int:
        '''
        ---> Recursive Solution <---
        if(n <= 1):
            return (n == 1)
        return n > 1 and self.fib(n-1) + self.fib(n-2)
        '''
        '''
        ---> Iterative Solution <---
        '''
        last_two = [0,1]
        count = 2
        while count <= n:
            sum = last_two[0] + last_two[1]
            last_two[0] = last_two[1]
            last_two[1] = sum
            count +=1
        
        return last_two[1] if n>0 else last_two[0]