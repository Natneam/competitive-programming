# LINK TO THE PROBLEM => https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = list()
        length = 0
        
        node = head
        while node:
            length += 1
            stack.append(node)
            node = node.next
    
        i = 1
        currNode = head
        while i < length:
            temp = currNode.next

            currNode.next = stack.pop()
            currNode.next.next = temp

            currNode = currNode.next.next

            i += 2

        currNode.next = None 
        
        
    
        
        
