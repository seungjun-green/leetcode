"""
Leet code 500. Keyboard Row Solution
Problem link: https://leetcode.com/problems/keyboard-row/

"""

class Solution:
    def findWords(self, words):
     
        output = []
        for word in words:
            if self.dd1(word) or self.dd2(word) or self.dd3(word):
                output.append(word)
            
        return output
        
        
        
    def dd1(self, word):
        group1 = "qwertyuiop"
        
        for character in word:
            if character.lower() not in group1:
                return False
        return True
            
    def dd2(self, word):
        group2 = "asdfghjkl"
            
        for character in word:
            if character.lower() not in group2:
                return False
        return True
            
    def dd3(self, word):
        group3 = "zxcvbnm"
            
        for character in word:
            if character.lower() not in group3:
                return False
        return True
