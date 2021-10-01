class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0
        else:
            for i in range(0, len(haystack) - length + 1):
                if haystack[i: i+length] == needle:
                    return i
        
        return -1
