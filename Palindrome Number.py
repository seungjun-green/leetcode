"""
Leet code: Palindrome Number
problem link: https://leetcode.com/problems/palindrome-number/
"""

# Solution
"""
convert the give integer into string, then compare at each end of character.
"""

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        for index in range(0, len(x) // 2):
                if x[index] != x[len(x) - 1 - index]:
                    return False
        return True
