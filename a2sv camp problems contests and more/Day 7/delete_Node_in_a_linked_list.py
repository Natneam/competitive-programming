# LINK TO THE PROBLEM => https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current = node
        prev = None
        while current:
            if current.next == None:
                if prev == None:
                    current = None
                else:
                    prev.next = None
                break
            current.val = current.next.val
            prev = current
            current = current.next
        