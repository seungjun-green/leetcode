'''
Time Complexity: O(n)

Algorithms
1. Convert given list into Sets(which has only distinct values)
2. Compare length of set and list, if they are same return False, otherwise retrun True
(because difference of those two length means, the list contains duplicate)

'''

class Solution:
    def containsDuplicate(self, nums):
        set1 = set(nums)
        
        if len(set1) != len(nums):
            return True
        else:
            return False

     
    
    
#TIP
'''
Time complexity can be slighly improved by checking whether same key exists while creating hashmap. - #TIP1 of MSDIF
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                return True
        return False
    
