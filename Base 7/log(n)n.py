"""
Leet code Base 7 Solution
Runtime: O(logn * n)

Solution: 
Divide given num by 7, and insert the String(remaining) to the list(answer).
Then return ''.join(answer)



"""


import math

class Solution:
    def convertToBase7(self, num: int) -> str:
        answer = []
        isMinus = False
        if num < 0:
            num = -num
            isMinus = True
            
            
            
        for i in range(0, int(math.log(num, 7)) + 1):
            add = num % 7
            answer.insert(0, str(add))
            num = num // 7
            
        if isMinus:
            answer.insert(0, '-')
            
            
        return ''.join(answer)
        
        
        
        
    
        
        
    
        
