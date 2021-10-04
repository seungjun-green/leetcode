# Solution1 - Brute Force
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        firstNum = 0
        secondNum = 0
        k1 = len(digits)
        for i in range(k1):
            firstNum += digits[i] * (10 ** (k1 - i - 1))
        
        res = []
        secondNum = firstNum + 1
        k = len(str(secondNum))
        temp = 0
        for i in range(k):
            temp = secondNum // (10 ** (k - i -1))
            secondNum -= temp * (10 ** (k - i -1))
            res.append(temp)
        
        return res
