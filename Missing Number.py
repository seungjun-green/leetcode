
"""
Problem Link: https://leetcode.com/problems/missing-number/
Get expected_sum and get current_sum of the given sum, the subtract current_sum from expected_sum
"""

class Solution:
    def missingNumber(self, nums):
        # get the list as an agrument
        
        # find the len of the list
        a = len(nums)
        expected_sum = 0
        
        current_sum = 0
       
        for i in range(0, a+1):
            expected_sum += i
            
        for element in nums:
            current_sum += element
        return expected_sum - current_sum
             
        
        
        
