"""
Leet code Remove Vowels from a String
Problem Link: https://leetcode.com/problems/remove-vowels-from-a-string/

Solution: 
Iterate over the given string(s), and if we founds the vowel character we replace that certain 'character' with '',
and then return the s
"""

class Solution:
    def removeVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for character in s:
            if character in vowels:
                s = s.replace(character, '')
                
        return s
