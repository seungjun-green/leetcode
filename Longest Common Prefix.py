"""
Leet code Longest Common Prefix Solution
Problem Link: https://leetcode.com/problems/longest-common-prefix/
"""

"""
Code Explaination:

Compare character one by one
"""


class Solution:
    def longestCommonPrefix(self, strs):
        n = len(strs[0])
        n2 = len(strs)
        answer = []
                
        a = strs[0]
        for i in range(0, n):
            c = a[i]
            
            for element in strs:
                if i >= len(element):
                    return "".join(answer)
                if c != element[i]:
                    return "".join(answer)
            answer.append(c)
            
        dd = "".join(answer)
        return dd
        
