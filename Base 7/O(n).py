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
            answer.append(str(add))
            num = num // 7
            
        if isMinus:
            answer.append('-') 
            
        return ''.join(answer[::-1])
    
    
    
    
        
        
        
        
    
        
        
    
        
