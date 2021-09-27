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
  Two pointers - this is possible, bc the input array is sorted in ascending order
  
  Time Complexity: O(n)
  Space Complexity: O(1)
  
  Algorithm
  1. Set two pointer at the first and end of the list
  2. As the list is already sorted in ascending order
  If 
  numbers[p1] + numbers[p2] < target: increment p1 by one
  numbers[p1] + numbers[p2] > target: decrease p2 by one
  numbers[p1] + numbers[p2] == target: return [p1+1, p2+1] - we add 1 to each element, only bc this problem define first index as 1, not 0
  '''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        
        while p1<p2:
            if numbers[p1] + numbers[p2] < target:
                p1+=1
            elif numbers[p1] + numbers[p2] > target:
                p2-=1
            else:
                return [p1+1, p2+1]
