"""
Leet code 3Sum Solution
Time Complexity: O(n^3)

Solution: Check every possible combination
"""



class Solution:
    def threeSum(self, nums):
        l = len(nums)
        result = [] #initallize the result list, which we will return as a answer
        for i in range(l):
            for j in range(l):
                for k in range(l):
                  # checking the condition given in this problem
                    if (i != j and i != k and j!= k) and i < j and j < k and (nums[i] + nums[j] + nums[k] == 0):
                        if self.fd(nums, result, i, j, k) == True:
                            result.append([nums[i], nums[j], nums[k]])
    
        return result
                      
      
      
      # function  that checking whether the 'result' already have same(all 6 combinations are considerd same) element
    def fd(self, nums, result, i, j, k):
           if ([nums[i], nums[j], nums[k]] not in result) and ([nums[i], nums[k], nums[j]] not in result) and [nums[j], nums[i], nums[k]] not in result and [nums[j], nums[k], nums[i]] not in result and [nums[k], nums[j], nums[i]] not in result and [nums[k], nums[i], nums[j]] not in result:   
                                           return True
                                           
                                           
        
        
