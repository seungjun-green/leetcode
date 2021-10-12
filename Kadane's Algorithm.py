# finding the maximum subarray


'''
idea:

the maximum subarray ending at index i is one of nums[i] or maximum subarray ending at index (i-1) + nums[i]


Algorithm:
1. iterating the nums, get the current current_max_subarray (maximum subarray ending at index i)
2. compare the current_max_subarray to global_max_subarray(for example, it could be maximum subarray ending at index i-4 or i-2 and so on)
3. after iteration return the global_max_subarray
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = nums[0]
        max_global = nums[0]
        
        for i in range(1, len(nums)):
            max_current = max(nums[i], max_current+nums[i])
            max_global = max(max_global, max_current)
            
        return max_global
