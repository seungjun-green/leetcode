"""
Leet code Pascal's Triangle Solution
Problem Link: https://leetcode.com/problems/pascals-triangle/

Solution: 
The function 'newLine' will take current line as an input and return next line. 
Append current line(start) tp the answer, then append the return value of 'newLine' function. Repeat this process for n(number of rows given) times.


Time Complexity: O(n^2)

newLine: n-2
for every n times=> n(n-2)
"""


class Solution:
    def generate(self, numRows):
        start = [1]
        answer = []
        
        for i in range(numRows):
            answer.append(start)
            start = self.newLine(start)
            
            
        return answer
        
    
    # get the new line of Pascal's Triangle
    def newLine(self, list):
        length = len(list) + 1
        result = [0] * length
        result[0] = 1
        result[length-1] = 1
        
        for i in range(1, length-1):
            result[i] = list[i] + list[i-1]
            
        return result
    
        
        
