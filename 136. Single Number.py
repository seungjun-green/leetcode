# Solution 1 - use hashtable

from collections import defaultdict

class Solution:
    def singleNumber(self, nums) :
        my_dict = defaultdict(int)
        
        print(my_dict)
        for element in nums:
            my_dict[element] += 1
            
        for key in my_dict:
            if my_dict[key] == 1:
                return key
              
  
  
 # Solution 2 - Bit Manipulation


'''
a⊕0=a
a⊕a=0

a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
