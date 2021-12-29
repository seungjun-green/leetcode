# Solution 1 - Brute Force

'''
Algorithm:
1. Create a new list
2. Create all possible substrings and append them to the newly created list
3. iterating the list, check whether the element(substring) consists of the unique alphabet. If it is check the length of it, and if it is bigger than the current max value,  update the value of maxValue
4. return max
'''


# TIP
# We improved Solution-1 by updating maxVlaue while creating all possible sub-strings. 
# In common way, we could have created list of all possible substring - O(n^2), then iterate the list again updating maxValue - O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(0, len(s)+1):
            for j in range(i, len(s)+1):
                temp = s[i:j+1]
                t2 = len(temp)
                if t2 > max and t2 == len(set(temp)):
                    max = t2
                    
        return max


    
      
# Solution 2 - sliding window


'''
1. Set left and right to 0
2. iterating the string, check whether current substring doesn't have any duplicates, update maxValue. 
If it is, increment left by 1, until condition becomes true.
3. After iteration ended, updatemaxValue.
'''


#TIP
# We improved time complexity of Solution 2 by not iterating every key values in hashmap, but checking only value of s[i]. 
# Because we already know values of other keys are smaller or equal to 1, and only value of s[i] is bigger than 1.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxValue = 0
        hashmap = {}


        def condition(hashmap, key):
            if hashmap[key] > 1:
                return False
            else:
                return True

            
        for i in range(len(s)):
            # update hashmap
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
                    
            if condition(hashmap, s[i]):
                maxValue = max(maxValue, right-left+1)
            else:
                while condition(hashmap, s[i]) == False:
                    hashmap[s[left]] -= 1            
                    left += 1 
                       
                
            right += 1      
    
        return maxValue
    
    
    
  # Solution 3 -  Advanced Sliding window
    
    class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        hashtable = {}
        
        i = 0
        
        for j in range(n):
            if s[j] in hashtable and i < hashtable[s[j]] + 1:
                i = hashtable[s[j]] + 1
                
            ans = max(ans, j-i+1)
            hashtable[s[j]] = j
            
        return ans
