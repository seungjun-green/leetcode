class Solution:
    def addBinary(self, a, b):
        result = self.bTd(a) + self.bTd(b)
        
        result = self.dTb(result)
        
        return result
        
    
    
    def bTd(self, s):
        l = len(s)
        result = 0
        for i in range(l):
            if s[i] == '1':
                result += pow(2, l-i -1)
        
        return result
    
    def dTb(self, d):
        result = 0
        count = 0
        while  d > 0:
        
            result += (d%2) * pow(10, count)
            d = d//2
            count += 1
        
        result = str(result)
        return result
        
