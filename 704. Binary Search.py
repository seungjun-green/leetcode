# Solution 1 - using iteration

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            pivot = start + (end - start) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                end = pivot - 1
            else:
                start = pivot + 1
        return -1

    
    
# Solution 2c-cusing recursion

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums,0,len(nums)-1,target)
        
    
    def binarySearch(self, nums, start,end, target):
        pivot = (start + end) //2
        if nums[pivot] == target:
            return pivot
        elif start >= end and nums[pivot] != target:
            return -1
        else:
            if nums[pivot] < target:
                return self.binarySearch(nums,pivot+1,end,target)   
            elif nums[pivot] > target:
                return self.binarySearch(nums,start,pivot-1,target)
