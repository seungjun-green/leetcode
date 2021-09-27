# Solution 1/2
'''
Time Complexity: O(n)
Memory Complexity: O(n)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)   
        nums2 = [0] * length
        
        for i in range(length):
            if i + k < length:                
                nums2[i+k] = nums[i]
            else:
                nums2[i+k-length] = nums[i]

        nums[:] = nums2
