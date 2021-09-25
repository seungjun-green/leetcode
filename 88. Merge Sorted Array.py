
# Solution - 1/3
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
        
        
# Solution - 2/3
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

                
# Solution - 3/3
'''
Time Complexity: O(n+m)
Space Complexity: O(1)

Alogrithm:
1. We don't have to store coopy of nums1 here.
2. Iterating from back of the nums2, and nums1[m-1], compare two element and put the bigger element to the nums1 from right to left.
'''        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        p1 = m - 1
        p2 = n - 1
    
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                
