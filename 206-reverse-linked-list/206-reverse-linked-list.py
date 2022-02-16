# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(curr):
            if not curr.next:
                return curr, curr #current node, head
            
            curr_node, head = reverse(curr.next)
            curr_node.next = curr
            curr.next = None
            return curr, head
            
        if not head:
            return None

        return reverse(head)[1]
    