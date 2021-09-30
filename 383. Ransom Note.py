'''
Algorithm:
1. create a hashmap, element as a key and how many time it appears as value, iterating string magazine
2. iterating ransomeNote, if the element does not exist or it's value is 0 return False, other then(if it exist in the hashmap) decrease the value by one
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashtable = {}
        hashtable = collections.Counter(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] not in hashtable or hashtable[ransomNote[i]] == 0:
                return False
            else:
                hashtable[ransomNote[i]] -= 1
                
        return True
