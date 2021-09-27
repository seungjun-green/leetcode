'''
Time Complexity: O(m*n)

Algorithm 
1. Convert given matrix into sinle list
2. Slicing the list by given K numbers make it as a row, make a new matrix
'''

class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        result = []
        answer = []
    
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                result.append(mat[i][j])
        print(result)
        
        if r*c != len(result):
            return mat
        
        subarray = []
        for i in range(len(result)):
            subarray.append(result[i])
            
            if (i+1)%c == 0:
                answer.append(subarray)
                subarray = []
                
        return answer
