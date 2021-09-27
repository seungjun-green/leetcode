# https://leetcode.com/problems/pascals-triangle/

'''
Time Complexity: O(numRows ^ 2)

'''


class Solution:
    def generate(self, numRows):
        ans = []
        row = [1]
        
        for i in range(numRows):
            ans.append(row)
            row = self.getNewRow(row, i+2)
            
        return ans
                    
     # func to get a new row   
    def getNewRow(self, preRow, length):
        newRow = [1] * length
        for i in range(1, length-1):
            newRow[i] = preRow[i-1] + preRow[i]
        return newRow
