# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1/2
'''
Time Complexity: O(n)

Algroithm:
1. Get the size of the linled list
2. Get the mid index
3. return the linked list from the mid index
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        size = 0
        while current_node.next != None:
            size += 1
            current_node = current_node.next
        size+=1
        
        midIndex = size//2
        
        c_node = head
        for i in range(midIndex):
            c_node = c_node.next
            print(c_node)
        
        return c_node
            
            
            
