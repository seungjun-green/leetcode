# https://leetcode.com/problems/roman-to-integer/
'''
Time Complexity: O(n)

If K th value is smaller than k+1 th one do subtaction, otherwise add the value to the total, do this iterating given string.

'''


Roman = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s):
        i = 0
        total = 0
        length = len(s)
        
        while i < length:
            if i + 1 < length and Roman[s[i]] < Roman[s[i+1]]:
                total = total + Roman[s[i+1]] - Roman[s[i]]
                i += 2
            else:
                total += Roman[s[i]]
                i += 1
                
        return total
                
        
