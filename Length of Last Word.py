"""
Leet code: Length of Last Word 
Problem Link: https://leetcode.com/problems/length-of-last-word/

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

Example 1:

Input: s = "Hello World"
Output: 5

Example 2:

Input: s = " "
Output: 0

"""

"""
Reverse string then iterate from 'start_index' until we met space(" ")

start_index is the index of first alphabet of reversed string, for example, if given string is "a tripple-bacon-cheeseburger   " 
the start_index will be 5
"""

class Solution:
    def lengthOfLastWord(self, s):
        new_s = s[::-1]
        new_list = []
        new_start = 0
        flag = False 
        for index in range(0, len(new_s)):
            if new_s[index] != " ":
                flag = True
                new_start = index
                break
                
        count = 0
        for index in range(new_start, len(new_s)):
            if new_s[index] == " ":
                break
            count += 1
                    
        return count     
