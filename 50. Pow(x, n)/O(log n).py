class Solution:
    def myPow(self, x, n: int):
        if n < 0:
            n = -n
            x = float(1)/float(x)
        return self.fastPower(x, n)
    
    def fastPower(self, x, n):
        if (n == 0):
            return 1.0
        
        a = self.fastPower(x, n // 2)

        if n % 2 == 0:
            return  a * a
        else:
            return a * a * x
        
