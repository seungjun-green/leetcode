# Solution 1 - Brute Force

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            tempSum = nums[i]
            if tempSum == k:
                result += 1
            
            for j in range(i-1,-1,-1):
                tempSum += nums[i]
                if tempSum == k:
                    result += 1
