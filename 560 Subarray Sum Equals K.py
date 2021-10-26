# Solution 1 - Brute Force

'''
Algorithm:
1. Create every possible sub array and check whether it's sum is equals to target sum,  if it does increment 'result' variable by 1
2. after iteration return the value of result variable
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(0,len(nums)):
            for j in range(i, len(nums)):
                temp = nums[i:j+1]
                current_sum = sum(temp)
                if current_sum == k:
                    result += 1
                
        return result
