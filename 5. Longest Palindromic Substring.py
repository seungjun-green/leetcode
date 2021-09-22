# https://leetcode.com/problems/longest-palindromic-substring/

'''
Time Complexity: O(n!)

Algorithm
1. Test all possible sub strings in from longest to shortest
2. If we found Palindromic one, return the sub string.
'''

class Solution:
    def longestPalindrome(self, s):
        longest = ""
        
        k = len(s)
        i = 0
        while k > 0:
            i = 0
            while i + k <= len(s):
                if self.isP(s[i:i+k]):
                    return s[i:i+k]
                i += 1
            k -= 1
            
    # function to check whether sub string is palindromic
    def isP(self, s):
        i = 0
        while i < len(s) / 2:
            if s[i] != s[len(s)- 1 - i]:
                return False
            i += 1
        return True
