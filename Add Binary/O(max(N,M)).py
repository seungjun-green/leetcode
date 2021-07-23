"""
Leet code Add Binary Solution
Problem Link: https://leetcode.com/problems/add-binary/

Solution: We will do addition by using ^(XOR), &(AND), << (Left-SHIFT), but not using '+'.


Example: 

When we do binary addition

1) if carry doesn't happens:

All the things we to do is just XOR of two operands. That's all we need too do.

2) But if Carray happens, we need to do some more few steps:

First, do XOR then add Carry.
The the next question might be, how can we add carry?

It's quite simple!


First think about procedure of adding carry in following case: 10 + 11 = 101.


Here carry(1) happens, at second spot, and we add it at third spot.

TO Simplift this, (1), find carry using &, then sift it to left one, then XOR it again.              
        
"""

class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        # BECAUSE IF THERE IS NO CARRY, the caculation will be ended right after one xor caculation
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
            
        return bin(x)[2:]
