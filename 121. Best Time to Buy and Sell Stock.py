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
'''    


class Solution:
    def maxProfit(self, prices):
        minPrice = 999999999
        maxProfit = 0
        for dayPrice in prices:
            if dayPrice < minPrice:
                minPrice = dayPrice
            if maxProfit < dayPrice - minPrice:
                maxProfit = dayPrice - minPrice
                
                
        return maxProfit
    
    
    
    
    
    
