class Solution:
    def countAndSay(self, n):
        s = '1'
        if n == 1:
            return s
        else:
            for i in range(n-1):
                s = self.next_number(s)
            return s
    
    def next_number(self,s):
        result = []
        i = 0
        
        while i < len(s):
            count = 1
            while i+1 < len(s) and s[i] == s[i+1]:
                i+=1
                count += 1
            result.append(str(count) + s[i])
            i+=1
        return ''.join(result)
    
        
