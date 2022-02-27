# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None
        
        head1 = self.sortList(head)
        head2 = self.sortList(temp)
        
        
        
        dummy_head = ListNode()
        curr_node = dummy_head
        
        while head1 or head2:
            if head1 and not head2:
                curr_node.next = ListNode(head1.val)
                head1 = head1.next
                
            if head2 and not head1:
                curr_node.next = ListNode(head2.val)
                head2 = head2.next
            
            if head1 and head2:
                if head1.val <= head2.val:
                    curr_node.next = ListNode(head1.val)
                    head1 = head1.next
                else:
                    curr_node.next = ListNode(head2.val)
                    head2 = head2.next
            curr_node = curr_node.next
        return dummy_head.next