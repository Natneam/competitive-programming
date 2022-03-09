# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-101)
        curr_node = dummy_node
        repeated_nodes = set()
        
        while head:
            if curr_node.val != head.val:
                curr_node.next = head
                curr_node = curr_node.next
            else:
                repeated_nodes.add(head.val)
                
            head = head.next
        
        curr_node = dummy_node
        
        while curr_node.next:
            if curr_node.next.val in repeated_nodes:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        
        
        return dummy_node.next
            