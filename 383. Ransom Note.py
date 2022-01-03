#Solution1

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap1 = collections.Counter(ransomNote)
        hashmap2 = collections.Counter(magazine)
        
        for key in hashmap1:
            if (key not in hashmap2) or key in hashmap2 and hashmap2[key] < hashmap1[key]:
                return False
        
        return True






#TIP
'''
You don't need to create two hashmaps for rasnomeNote and magazine. Just create one hashmap for magazine(key as character, value as numer of appearance).
Iterating the hashmap, check the condition. 
'''

#Soultion2
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
