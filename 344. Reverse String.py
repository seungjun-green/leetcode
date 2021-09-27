# Solution 1/2

'''
Time xomplexity: O(n)
Space Complexity: o(1)

Algorithm :
1. set p1 to 0, and p2 end of index
2. while p1 < p2: swap s[p1] and s[p2] and p1+=1, p2-=1
'''

class Solution:
    def reverseString(self, s):
        p1 = 0
        p2 = len(s)-1
        
        while p1<p2:
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        
        return s
