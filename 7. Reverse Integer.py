# https://leetcode.com/problems/reverse-integer/
'''
Time Complexity: O(n)

Algroithms
1. If given number(x) is minus, make it plus and set abs to True
2. Convert the x into string
3. Iterating the string, do following: result += int(x[i]) * 10 ** i
4. if abs is True, put the minus again
5. if result is in 32bit range, return result otherwise return 0
'''

class Solution:
    def reverse(self, x):
        abs = False
        if x < 0:
            abs = True
            x = -x

        result = 0
        x = str(x)
        
        a = len(x)
        for i in range(a):
            result += int(x[i]) * 10 ** i

        if abs:
            result = -result
        
        ov = 2**31
            
        if result > ov-1 or result < -ov:
            return 0
        else:
            return result  
