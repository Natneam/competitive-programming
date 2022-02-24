# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        vals.sort()
        
        dummy_node = ListNode()
        curr_node = dummy_node
        for val in vals:
            curr_node.next = ListNode(val)
            curr_node = curr_node.next
        
        return dummy_node.next