'''
Algorithm:
dp[i] = dp[i-1] + dp[i-2]
'''

# Solution 1 - using recursion
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


# Soltion 2 0 iterative way
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
