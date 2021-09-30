# Solution1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}   
        # creat hashtable
        # key : element
        # value: number of element in the given string
        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable[s[i]] = 0
            else: 
                hashtable[s[i]] += 1
        
        # iterating hashtable, if we found value 0, return the index of the key in the given string
        for key in hashtable:
            if hashtable[key] == 0:
                return s.index(key)
        return -1
