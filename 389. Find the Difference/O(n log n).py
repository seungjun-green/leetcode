"""
Leet code Find the Difference Solution
Problem Link: https://leetcode.com/problems/find-the-difference/

Description: Sort two list(s, t) and compare one by one untill we found different one.
"""

class Solution:
    def findTheDifference(self, s, t):

        # Sort both the strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # Character by character comparison
        i = 0
        while i < len(s):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]
            i += 1

        return sorted_t[i]
