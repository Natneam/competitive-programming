# LINK TO THE PROBLEM => https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = self._lenOfLinkedList(head)
        # print(length)
        # print(self._reverseLinkedList(head))
        i = 1
        curr_head = head
        while i <= length//2:
            i+=1
            curr_head = curr_head.next
        curr_head = curr_head if length % 2 == 0 else curr_head.next
        new_head = self._reverseLinkedList(curr_head)
        
        i = 1
        curr_head = head
        while i <= length//2:
            i+=1
            if curr_head.val != new_head.val:
                return False
            curr_head = curr_head.next
            new_head = new_head.next
        return True

        
        
    def _lenOfLinkedList(self, head):
        curr_head = head
        length = 0
        while curr_head:
            length += 1
            curr_head = curr_head.next
        return length
    def _reverseLinkedList(self, head):
        curr_head = head
        prev = None
        while curr_head:
            nextTemp = curr_head.next
            curr_head.next = prev
            
            prev = curr_head
            curr_head = nextTemp
        return prev
    
#             recursive approch
#         try:
#             self._reverse(head, head)
#         except ValueError:
#             return True
#         except:
#             return False
#         return True

#     def _reverse(self, head, curr_head):
#         if not curr_head:
#             raise ValueError
#         elif not curr_head.next:
#             if head.val != curr_head.val:
#                 raise Exception()
#             return head.next
#         new_head = self._reverse(head, curr_head.next)
#         if new_head.val != curr_head.val:
#             raise Exception
        
#         return new_head.next