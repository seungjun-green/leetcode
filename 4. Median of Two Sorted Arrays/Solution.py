# https://leetcode.com/problems/median-of-two-sorted-arrays/

'''

Time Complexity: O(n logn)

Algorithm

1. merge two lists
2. Sort the merged list in ascending order
3. if len of the merged is
    odd : return items at middle index
    
    even: return average of two items at middle
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        merged = nums1 + nums2
        merged.sort()
        
        length = len(merged)
        
        if length % 2 != 0:
            return merged[length//2]
        else:
            return (merged[int((length-1)/2 - 0.5)] + merged[int((length-1)/2 + 0.5)]) / 2
        
