# Solution 1/2

'''
Time Complexity: O(n)
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = [0] * len(nums)
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums2[j] = nums[i]
                j+=1
    
        nums[:] = nums2
        
