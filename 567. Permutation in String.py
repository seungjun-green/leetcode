# Solution 1 - Brute Force

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
            
