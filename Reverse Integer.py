"""
Leet code - Reverse Integer Solution
problem link: https://leetcode.com/problems/reverse-integer/
"""

class Solution:
    def reverse(self, x):
        if x >= pow(2, 31) - 1 or x <= -pow(2, 31):
            return 0
        
        s = str(x)
        # when given iteger is minus
        if s[0] == '-':
            pass
            s = s[1:]
            s = s[::-1]
            x = int(s)
            x = -x
            if x >= pow(2, 31) - 1 or x <= -pow(2, 31):
                return 0
            return x
        
        # when given integer is + value
        else:
            s = s[::-1]
            x = int(s)
            if x >= pow(2, 31) - 1 or x <= -pow(2, 31):
                return 0
            return x
      
      
"""
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""
