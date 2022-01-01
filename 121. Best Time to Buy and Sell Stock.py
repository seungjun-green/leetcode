# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution - 1/2
'''
Time Complexity: O(n^2)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max:
                    max = profit
        return max
    
    

# Solution - 2/2
'''
Time Complexity: O(n)
Algorithm: use SJ'S Algorithm[MDS]
'''    

import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_min = prices[0]
        current_max = 0
        global_max = -math.inf
        
        for i in range(1, len(prices)):
            current_max = prices[i] - global_min
            global_max = max(global_max, current_max)
            global_min = min(global_min, prices[i])
    
        
        if global_max > 0:
            return global_max
        else:
            return 0
    
    
    
    
