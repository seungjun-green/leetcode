"""
Leet code Two Sums Solution
Problem Link: https://leetcode.com/problems/two-sum/solution/
Solution: Use dictionary


given list: [2, 7, 11, 15]

make a new dictionary: {2: 0, 7: 1, 11:2, 15: 3}
                        ^        ^
                        |        |
                        Key    Value
        
*for key we set the element of the list.
*for value we set the index number of the element in the list.
                        
                        
 Then start iterating the list(nums) doing following:
 
Get the complement and check whether then search dict whetehr the complement(key exist) 
 and aslo check whether the 'value of the key'(index in nums) have different value.
 



|---------------------------------------------------------------------|
| Time Complexity of Searching Key in Dictionary is O(1), constant time. 
|
|    ex.) if key in dict:
|          do stuff
|
|---------------------------------------------------------------------|

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        
        #creating a dictionary
        for index in range(0, len(nums)):
            dict[nums[index]] = index
            
        print(dict)
            
        
        for index in range(0, len(dict)):
            #get the complement
            complement = target - nums[index]
            
            # check  if complement exist in the dictionary and 
            # check if the complement has same index as current index(in terms of 'nums' list)
            if complement in dict and dict[complement] != index:
                
                return [index, dict[complement]]
                        
