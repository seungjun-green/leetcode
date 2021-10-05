# Solution 1 - Brute Force


'''
Algorithm:
1. get sum of all possible combination of 1 and 2
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        k = n//2
        res = 0
        print("k", k)
        for i in range(k+1):
            temp = n - i*2
            res += self.factorial(i+temp) // (self.factorial(i) * self.factorial(temp))
            
            
            
        return res
            
    
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            return n * factorial(n-1)


# Solution 2 - Dynamic Programming

'''
Algorithm:

dp[i] = dp[i-1] + dp[i-2]

'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            print(dp[i-1], dp[i-2])
            dp[i] = dp[i-1] + dp[i-2]
        
        
        return dp[n]
