# Solution 1
 '''
 Time Complexity: O(n)
 
 Algorithm: Linear Search
 '''
  class Solution:
    def firstBadVersion(self, n):
        for i in range(1, n+1):
            if isBadVersion(i):
                return i

# Solution 2
 '''
 Time Complexity: O(log n)
 
 Algorithm: Binary Search
 '''
 
 class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start < end:
            mid = (start+end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start
