"""
Leet Code Best Time to Buy and Sell Stock Solution
Problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description: 
Set the minPrice as highest value of interger. then iterate the given array update the minPrice
And in same iteration, update the maxProfit by comparing maxProfit and todayPrice - minPrice.

After iteration return the maxProfit
"""


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
