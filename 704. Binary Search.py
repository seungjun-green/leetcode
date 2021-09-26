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
