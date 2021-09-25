
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
'''
Time Complexity: O(n+m)

Alogrithm:
1. copy nums1[:m] to nums1Copy
2. comparing one element in nums1Copy and one element nums2 left to right, input smaller one to nums1. 
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1Copy = nums1[:m]
        pr1 = 0
        pr2 = 0
        pw = 0
        
        for pw in range(n+m):
            if pr2 >= n or (pr1 < m and nums1Copy[pr1] <= nums2[pr2]):
                nums1[pw] = nums1Copy[pr1]
                pr1+=1
            else:
                nums1[pw] = nums2[pr2]
                pr2 += 1
