
# Solution 1 - Brute Force
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 1
        if n == 0:
            return 0
        while n != 1:
            temp = n%2
            
            if temp == 1:
                count += 1
            
            n = n // 2

        return count
    
    
    
 # Solution 2 - Bit Manipulation  
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            n = n & (n-1)
            count += 1
        
        return count
