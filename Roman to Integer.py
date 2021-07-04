"""
leet code Roman to Integer Solution
Problem Link: https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s):
        answer = 0
        prev = 1001
        
        for element in s:
            print(answer)
            if self.convert(element) <= prev:
                answer += self.convert(element)
                prev = self.convert(element)
            else:
                answer += self.convert(element)
                answer -= 2*prev
                prev = self.convert(element)
            
        return answer
            
     
    def convert(self, element):
        if element == 'I':
            return 1
        if element == 'V':
            return 5
        if element == 'X':
            return 10
        if element == 'L':
            return 50
        if element == 'C':
            return 100
        if element == 'D':
            return 500
        if element == 'M':
            return 1000
