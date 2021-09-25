'''
Solution - 1/2

Time Complexity:  O(n^2)

Algorithm:
1. Get the sum of all possible sub arrays.
2. keep updating maxA while getting sum of all possible sub arrays
3. after end of iteration, return maxA
'''

class Solution:
    def maxSubArray(self, nums):
        maxA = -math.inf
        sumA = 0
        for k in range(1, len(nums)+1):
            for i in range(len(nums)-k+1):
                sumA = sum(nums[i:i+k])
                if sumA > maxA:
                    maxA = sumA
                    
        return maxA

    
    
    
'''
Solution - 2/2
Time Complexity: O(n)

Algorithm - use Kadane's algorithm
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_max = []
        max_list = []
        for i in range(len(nums)):
            if i == 0:
                pre_max = [nums[i]]
                max_list = [nums[i]]
            if i > 0:
                pre_max = max(pre_max + [nums[i]], [nums[i]])

            if sum(pre_max) > sum(max_list):
                max_list = pre_max.copy()

        return sum(max_list)
