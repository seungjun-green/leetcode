# https://leetcode.com/problems/reverse-integer/
'''
Time Complexity: O(n)

Algroithms
1. Store the given num in hashmap like following:
493 => {'0':4, '1':9, '2':3}
2. do this ' result += value * 10 ** key' iterating hashmap
3. if result is not in range of [-2^31, 2^31], return 0, otherwsie return the result
'''

class Solution:
    def reverse(self, x):
        abs = False
        if x < 0:
            abs = True
            x = -x
            
        hashmap = {}
        
        a = len(str(x))
        for i in range(a):
            hashmap[i] = x//(10**(a-i-1))
            x -= (x//(10**(a-i-1))) * 10 ** (a-i-1)        
            
        print(hashmap)
        result = 0
        for i in range(len(hashmap)):
            result += hashmap[i] * 10 ** i
        
        if abs:
            result = -result
            
        if result > 2**31 or result < -2**31:
            return 0
        else:
            return result
  
