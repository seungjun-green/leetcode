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
