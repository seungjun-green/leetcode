'''
Algorithm:

If the next character c is a letter, then we will duplicate all words in our current answer, 
and add lowercase(c) to every word in the first half, and uppercase(c) to every word in the second half.


S = 'a1b2'

[[a], [A]]
[[a,1], [A,1]]
[[a,1], [A,1], [a,1]]
[[a,1, b], [A,1], [a,1, B]]
[[a,1, b], [A,1], [a,1, B], [A,1]]
[[a,1, b], [A,1, b], [a,1, B], [A,1, B]]
'''


class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        return map("".join, ans)
