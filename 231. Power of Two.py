# Solution 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n <= 0:
            return False
        
        while n>1:
            if n%2 != 0:
                return False
            else:
                n = n // 2       
                
        return True
    
    
    
 
# Solution 2 - Bit Manipulation


'''

2^0 = 1
2^1 = 10
2^2 = 100
2^3 = 1000


x & (-x) ==> keep the right most 1-bit and set all other bits to 0
[computer use 2's complement]

'''

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return (n & (-n)) == n
