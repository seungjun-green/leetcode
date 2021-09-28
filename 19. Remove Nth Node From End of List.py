# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1/2
'''
Time Complexity: O(n)

Algorithm:
1. Find the length of the Linked List
2. As we are using single linked list we can't traverse from back, so assign size-n to n. So that we can remove (size-n) th node
3. remove (size-n) th node
'''
class Solution:
    def removeNthFromEnd(self, head, n):
        print(head)
        size = 0
        current_node = head
        
        while current_node.next != None:
            size += 1
            current_node = current_node.next
        size+=1
        print(size)
        n = size - n
        if n == 0:
            return head.next
        
        current_node = head
        for i in range(n):
            if i == n-1:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
           
        print(head)  
        return head
