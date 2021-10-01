
# Solution 1 - Brute Force
'''
Algorithm:
1. get the length of s1
2. We create len(s2) - length numbers of substring, checcking whetehr each substring can be permutaion string of s1. If we found one retrun True
3. If we didn't find any one, return False
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        temp = ""
        hash1 = collections.Counter(s1)
        
        for i in range(0, len(s2) - length + 1):
            temp = s2[i: i+length]
            hash2 = collections.Counter(temp)
            
            if hash1 == hash2:
                return True
        
        return False
            
