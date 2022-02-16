# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        
        curr_node = dummy_node
        while curr_node.next and curr_node.next.next:
            node1 = curr_node.next
            node2 = curr_node.next.next
            node3 = curr_node.next.next.next
            
            node1.next = node3
            node2.next = node1
            curr_node.next = node2
            
            curr_node = curr_node.next.next
        
        return dummy_node.next