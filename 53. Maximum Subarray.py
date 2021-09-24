'''
Time Complexity:  O(n^2)
1. Get the sum of all possible sub arrays.
2. keep updating maxA while getting sum of all possible sub arrays
3. after end of iteration, return maxA
'''

class Solution:
    def maxSubArray(self, nums):
        maxA = -10000
        sumA = 0
        for k in range(1, len(nums)+1):
            for i in range(len(nums)-k+1):
                sumA = sum(nums[i:i+k])
                if sumA > maxA:
                    maxA = sumA
                    
        return maxA
