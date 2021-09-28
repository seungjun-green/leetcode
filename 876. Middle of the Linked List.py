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
            
            
# Solution 2

'''
Time Complexity: O(n)

Algorithm:
1.move slow by one node, fast by two node
2.when fast node or next next of fast reaches the end, slow pointer will be at the middle of the linked list
3.return linked list from slow node.

'''
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
            
