"""
Leet Code Powe(x, n) Solution
Problem Link: https://leetcode.com/problems/powx-n/

Description: 'Use recursion'

idea: 
Nobs: x * x * x * x ...... x =  x ^ n
Pro: x^(n/2) * x^(n/2) = x ^ n
==> keep calling fastPower(x, n//2) untill we reache the base case

"""

class Solution:
    def myPow(self, x, n: int):
        if n < 0:
            n = -n
            x = float(1)/float(x)
        return self.fastPower(x, n)
    
    def fastPower(self, x, n):
        #base case
        if (n == 0):
            return 1.0
        
        a = self.fastPower(x, n // 2)

        if n % 2 == 0:
            return  a * a
        else:
            return a * a * x
        
