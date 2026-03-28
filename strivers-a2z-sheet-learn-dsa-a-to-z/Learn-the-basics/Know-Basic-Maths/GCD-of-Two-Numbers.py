# https://takeuforward.org/plus/dsa/problems/gcd-of-two-numbers?source=strivers-a2z-dsa-track

"""
Euclidean Algorithm:
The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
of two numbers. It operates on the principle that the GCD of two numbers remains
the same even if the smaller number is subtracted from the larger number.

n1 = 20, n2 = 15

gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
gcd(5, 15)  = gcd(15 - 5, 5)  = gcd(10, 5)
gcd(10, 5)  = gcd(10 - 5, 5) = gcd(5, 5)
gcd(5, 5)   = gcd(5 - 5, 5)  = gcd(0, 5)

GCD = 5
"""
class Solution:
    def GCD(self, n1, n2):
        while(n1>0 and n2>0):
            if(n1>=n2):
                n1 = n1%n2
            else:
                n2 = n2%n1
            if(n1==0):
                return n2
            elif(n2==0):
                return n1