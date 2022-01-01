'''
Time Complexity: O(m*n)

Algorithm 
1. Convert the given matrix into single list
2. Create a new matrix with R number of lists with C number of elements in it.
'''

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nums = []
        # converting given matrix into a single list
        for array in mat:
            for element in array:
                nums.append(element)
        
        temp = []
        answer = []
        
        # ireshape operation with given parameters is not possible return original matrix.
        if r*c != len(nums):
            return mat
        
        # creating a new matrix with the single list
        for i in range(r):
            for j in range(c):
                temp.append(nums[i*c+j])
            
            answer.append(temp)
            temp = []
        
        
        return answer
