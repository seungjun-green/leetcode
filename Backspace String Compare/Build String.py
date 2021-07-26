"""
Leet code Backspace String Compare Solution
Problem Link: https://leetcode.com/problems/backspace-string-compare/solution/

Time Complexity: O(n+m)
Space Complexity: O(n+m)
Solution: 
"""


class Solution:
    def backspaceCompare(self, s, t):
        s = self.reframe(s)
        t = self.reframe(t)
        
        if s == t:
            return True
        else:
            return False
        
        
        
    def reframe(self, str):
        new_str = []
        count = 0
        for index in range(len(str)):
            if str[index] == "#":
                if count < 1:
                    pass
                else:
                    print(index - count)
                    new_str.pop(count-1)
                    count -= 1
         
            else:
                new_str.append(str[index])
                count += 1
                
        return ''.join(new_str)
            
            
        
