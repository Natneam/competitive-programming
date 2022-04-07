# LINK TO THE  PROBLEM => https://leetcode.com/problems/reverse-linked-list/

# from copy import deepcopy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode, index=0):        
        # reversing linked list iterativly 
        
        newHead = None
        current = head
        while current != None:
            temp = newHead
            newHead = ListNode(current.val)
            newHead.next = temp
            current = current.next
        return newHead
    
        # reversing linked list recursively

#         if not head: #case for empty LinkedList
#             return head
#         if head.next == None: #base case for the last call
#             if index == 0:
#                 return head
#             return head,head
#         else:
#             after,top = self.reverseList(head.next, index+1)
#             after.next = head
#             if index == 0:
#                 head.next = None
#                 return top
#             return head,top
        
        