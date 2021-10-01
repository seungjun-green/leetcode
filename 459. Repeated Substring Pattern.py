class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length):
            if length%i != 0:
                continue
                
            check = True
            temp = s[0:i]
            
            for j in range(0, length-i+1, i):
                if temp != s[j:j+i]:
                    check = False
                    break
                
                #temp = s[j:j+i]
                # You don't need to keep updating the temp, bc if temp was different from previous one, the current loop was already exited due to break keyword
            
            if check:
                return True
        
        return False
