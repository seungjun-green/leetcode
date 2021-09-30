class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable1 = collections.Counter(s)
        hashtable2 = collections.Counter(t)
        
        if len(hashtable1) != len(hashtable2):
            return False
        
        for key in hashtable1:
            if hashtable1[key] != hashtable2[key]:
                return False
        return True
