"""
Leet code Build Array from Permutation Solution
Problem Link: https://leetcode.com/problems/build-array-from-permutation/

Description: 
Create an emptry array(ans), then add new element following the rule: ans[i] = nums[nums[i]]

"""

class Solution:
    def buildArray(self, nums):
        ans = [None] * len(nums)
        for element in nums:
            ans[element] = nums[nums[element]]
        
        
        return ans
        
