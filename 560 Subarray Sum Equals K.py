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
    
    
    

    
# Solution 2 - cumulative sum
'''
- Improved Solution1 in a way getting sum of sub array
- Instead of getting every sum of each sub array we can do:
sumToElement[j] - sumToElement[i-1] == sum(nums[i:j+1])
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_list = [0] * (len(nums) + 1)
        result = 0
        curr_sum = 0 
        for i in range(len(nums)):
            curr_sum += nums[i]
            sum_list[i+1] = curr_sum
        
        temp_sum = 0  # sum of subarray
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                temp_sum = sum_list[j+1] - sum_list[i]
                if temp_sum == k:
                    result += 1
                    
        return result
    
    
    
    
# Solution3 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        tempSum = 0
        count = 0
        for i in range(len(nums)):
            tempSum += nums[i]
            
            if tempSum-k in hashmap:
                count += hashmap[tempSum-k]
                
            if tempSum in hashmap:
                hashmap[tempSum] += 1
            else:
                hashmap[tempSum] = 1
            
            if tempSum == k:
                count += 1
            
            
        return count
