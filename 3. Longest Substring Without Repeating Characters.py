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

    
    
 # Solution 2 - Advanced Brute Force Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for l in range(1, len(s)+1):
            for i in range(0, len(s)-l+1):
                temp = s[i:i+l]
                t2 = len(temp)
                if t2 > max and t2 == len(set(temp)):
                    max = t2
                    
        return max

    
    
    
# Solution 3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        
        left = right = 0
        
        res = 0
        
        
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1
            
            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1
                
            res = max(res, right-left+1)
            
            right += 1
        
        return res
