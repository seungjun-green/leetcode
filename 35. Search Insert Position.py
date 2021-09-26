class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
        pivot = -1
        while left < right:
            pivot = (left + right) // 2
            if nums[pivot] > target:
                right = pivot - 1
            elif nums[pivot] < target:
                left = pivot + 1
            else:
                return pivot
        
        if target > nums[left]:
            return left + 1
        else:
            return left
  
        
