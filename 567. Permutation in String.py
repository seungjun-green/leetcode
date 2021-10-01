
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
            

        
# Solution 2 - (sliding window)advaencd version of solution 1
'''
Algorithm:
Instead of creating a new hashmp for every new substring, keep updating hashmap:
if substrig moved from [i, j) to [i+1, j+1):
hashamp[i] -= 1 (or delete)
hashmap[j+1] += 1

'''


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        temp = ""
        hash1 = collections.Counter(s1)
        
        t = s2[0]
        temp = s2[0: length]
        hash2 = collections.Counter(temp)
            
        for i in range(0, len(s2) - length + 1):
            
            if i != 0:
                hash2[t] -= 1
                if hash2[t] == 0:
                    hash2.pop(t)
                
                hash2[s2[i+length-1]] += 1
            
            
            t = s2[i]
            if hash1 == hash2:
                return True
        
        return False
