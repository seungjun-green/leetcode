# Solution 1/2

'''
Time Complexity:O(N)
Algorithm:
1. Iterating linked list l1, create num1.
2. Iterating linked list l2, create num2.
3. Get num1+num2, and get reverse of it. => b 
4. Iterating b, create a new linked list, each digit as a value
'''

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        size1 = 0
        size2 = 0
        
        current_node = l1
        while current_node != None:
            num1 += current_node.val * (10 ** size1)
            size1 += 1
            current_node = current_node.next
    
        current_node = l2
        while current_node != None:
            num2 += current_node.val * (10 ** size2)
            size2 += 1
            current_node = current_node.next
        
        a = 0
        b = (str(num1+num2))[::-1]
        c = len(b)
        b = int(b)
        
        prehead = ListNode(-1)
        current = prehead

        currentNode = prehead
        for i in range(c):
            k = 10 ** (c-i-1)
            a = b // k
            b -= a * k
            current.next = ListNode(a)
            current = current.next
     
        return prehead.next
