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
      
      
# Solution 2 - BFS

'''
Algorithm:
1. iterating given matrix
    if mat[r][c] == 0:
        q.append([r,c])
    if mat[r][c] == 1:
        mat[r][c] = '#'
        
        
2. iterating q,do BFS once per element.
if we found # in mat[nr][nc]

update mat[nr][nc] = mat[i][j] += 1
and append the [nr, nc] to the q
'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        q = []
        
        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append([i, j])
                else:
                    mat[i][j] = "#"
        
        for row, column in q:
            for dx,dy in (1,0), (-1,0), (0,1), (0,-1):
                nr = row + dx
                nc = column + dy
                
                if 0<= nr < height and 0 <= nc < width and mat[nr][nc] == "#":
                    mat[nr][nc] = mat[row][column] + 1
                    q.append([nr, nc])
                    
                    
        return mat
