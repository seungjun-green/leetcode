
"""
Leet code Two Sums Solution
Problem Link: https://leetcode.com/problems/two-sum/solution/

Solution: Check every possible combinaton

"""


class Solution:
    def twoSum(self, nums, target):
        answer = []
        for i in range(0, len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer.append(i)
                    answer.append(j)
                    return answer
