
# Solution - 1/2
"""
Time Complexity: O((n+m) * log(n+m))
- The cost of sorting a list of length xx using a built-in sorting algorithm is O(x * logx )

Algorithm
1. Merge two list
2. the sort the merged list
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[i + m] = nums2[i]
        nums1.sort()
        
        
# Solution - 2/2
"""
Time Complexity: O((n+m))

Algorithm

"""
