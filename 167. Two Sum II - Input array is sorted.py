# Solution 1/2 

'''
Hashmap

Time Complexity: O(n)
Space Complexity: O(n)

Algorithm:
1. Create a hashmap
2. iterating hashmap, create complement of current element, and if the complement exist in hashmap, return [ current index, and value of the complement in hashmap]
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(numbers)):
            hashmap[numbers[i]] = i+1
            
        for i in range(1, len(numbers)+1):
            complement = target - numbers[i-1]
            if complement in hashmap:
                return [i, hashmap[complement]]
              
              
   # Solution - 2/2
  
  '''
  Two pointers
  
  '''
