"""
Leet code Single Number Solution
Problem Link: https://leetcode.com/problems/single-number/

Description: iterate the list one by one, checking the number of the certain element in the list(by function 'n').
If the return value of function 'n' is bigger than 2 then pass,if it is 1, then singleNumber function(main function) return that element.
And we get the answer.
"""

class Solution:
    def singleNumber(self, nums) :
        for element in nums:
            if self.n(nums, element) >= 2:
                pass
            else:
                return element
        
    def n(self, list, element):
        count = 0
        for index in range(0, len(list)):
            if list[index] == element:
                count +=1
            
        return count
