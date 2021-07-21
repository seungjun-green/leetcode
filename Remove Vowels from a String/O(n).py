

class Solution:
    def removeVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for character in s:
            if character in vowels:
                s = s.replace(character, '')
                
        return s
