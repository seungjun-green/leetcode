# Solution 1 - Brute Force

'''

'''

class Solution:
    def updateMatrix(self, mat):
        R = len(mat)
        C = len(mat[0])
        dist = [[math.inf] * C for i in range(R)]

        if R == 0:
            return mat
        
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                
                else:
                    for i in range(R):
                        for j in range(C):
                            if mat[i][j] == 0:
                                dist[r][c] = min(dist[r][c], abs(i-r) + abs(j - c))
        
        return dist
      
      
      
      
