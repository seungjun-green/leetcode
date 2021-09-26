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
