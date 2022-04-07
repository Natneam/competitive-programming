# LINK TO THE PROBLEM => https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # finding the length of the linked list
#         length = 0
#         current = head
#         while (current!= None):
#             length += 1
#             current = current.next
        
#         current = head
#         index = 1
#         while (index < (length// 2) + 1):
#             index+=1
#             current = current.next
#         return current
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        