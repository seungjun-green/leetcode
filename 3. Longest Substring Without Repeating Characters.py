# Solution 1 - Brute Force

'''
Algorithm:
1. Create a new list
2. Create all possible sub strings and append it as an element of newly created list
3. iterating the list, check wheteher the string consist of only unique alphabet, if it is then check len of it, and if is bigger than current max,  update the value of max
4. return max
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        for l in range(1, len(s)+1):
            for i in range(0, len(s)-l+1):
                subs.append(s[i:i+l])
        
        max = 0
        for ss in subs:
            if len(ss) != len(set(ss)):
                continue
            if len(ss) == len(set(ss)) and len(ss) > max:
                max = len(ss)
        
        return max
