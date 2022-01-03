class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square every element
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        
        # sort the array
        nums.sort()
        return nums
