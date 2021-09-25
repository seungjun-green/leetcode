'''
Time Complexity: O(n)

Algorithm
1. Create a hashmap, ket as element of nums and value as index of the element
2. Iterating nums, get the complement of current element, then check whether the complement exists in the hashamp. if it exists return
[current index of element, value of complement]

'''


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
