'''
    Time Complexity: O(n^2)
    
    Algorithm
    
    1. Initallize max as -1
    2. Iterate all possible sum, updating max value if sum > max and max < k
    3. after iterating all possible sum, return value of the max
    
'''

class Solution:
    def twoSumLessThanK(self, nums, k):
        max = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum > max and sum < k:
                    max = sum
        
        return max 
