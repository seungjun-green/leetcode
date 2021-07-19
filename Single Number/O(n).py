"""
Leet code Single Number Solution
Problem Link: https://leetcode.com/problems/single-number/
"""

from collections import defaultdict

class Solution:
    def singleNumber(self, nums) :
        my_dict = defaultdict(int)
        
        # creating a dictionary
        # key here is the element, and value is the count of the element in the given list
        for element in nums:
            my_dict[element] += 1
            
        #iterate over dictionary untill we found the value of key is 1.
        for key in my_dict:
            if my_dict[key] == 1:
                return key
