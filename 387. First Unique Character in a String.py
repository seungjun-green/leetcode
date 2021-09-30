# Solution1
'''
Algorithm - same for Sol1 and Sol2

1. Create aa hashamp, element as key and how many time appears as value
2. iterating the hashmap, if we found the key which it's value is 1, then return the index of the element(key) in the string
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}   
        # creat hashtable
        # key : element
        # value: number of element in the given string
        for i in range(len(s)):
            if s[i] not in hashtable:
                hashtable[s[i]] = 1
            else: 
                hashtable[s[i]] += 1
        
        # iterating hashtable, if we found value 0, return the index of the key in the given string
        for key in hashtable:
            if hashtable[key] == 1:
                return s.index(key)
        return -1

    
    
# Solution 2
# building the hashtable using collections.Counter is much more faster!

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable = {}   
        
        hashtable = collections.Counter(s)
        
        for key in hashtable:
            if hashtable[key] == 1:
                return s.index(key)
        return -1
