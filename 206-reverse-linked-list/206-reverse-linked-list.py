# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        stack = []
        
        while head:
            stack.append(head)
            head= head.next
        
        node = stack.pop()
        curr_node = node
        while stack:
            curr_node.next = stack.pop()
            curr_node = curr_node.next
        curr_node.next = None
        
        return node