# https://leetcode.com/problems/valid-parentheses/
'''
Time Complexity: O(n)

Algorithms
1. Create an Stack
2. Put the parthness to the stack, then check whether element at the top and element before the top are valid parthness, if they are pop those two elements, iterating given string
3. At the end of iteration, if len of stack is 0 return true otherwise return false

'''

hashmap = {
    '(':1,
    ')':6,
    '[':3,
    ']':4,
    '{':2,
    '}':5
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        k = 0
        for i in range(len(s)):
            stack.append(s[i])
            k += 1
            if k > 1:
                if hashmap[stack[k-1]] + hashmap[stack[k-2]] == 7 and hashmap[stack[k-2]] < hashmap[stack[k-1]]:
                    stack.pop()
                    stack.pop()
                    k -= 2
                
        
        if len(stack) == 0:
            return True
        else: 
            return False
