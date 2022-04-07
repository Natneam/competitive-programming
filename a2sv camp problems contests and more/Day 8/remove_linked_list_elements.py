# LINK TOO THE PROBLEM => https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr_node = head
        prev_node = None
        while curr_node:
            if curr_node.val == val:
                if curr_node == head:
                    head = head.next
                    curr_node = head
                    # print(curr_node.val)
                    continue
                else:
                    prev_node.next = curr_node.next
                    curr_node = curr_node.next
                    continue
            
            prev_node = curr_node
            curr_node = curr_node.next
        return head