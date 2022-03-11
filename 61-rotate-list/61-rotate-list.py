# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        #find length
        curr_node = head
        length = 0
        
        while curr_node:
            curr_node = curr_node.next
            length += 1
        
        k = k % length
        
        if k == 0:
            return head
        
        dummy_head = ListNode()
        dummy_head.next = head
        
        fast = dummy_head.next
        slow = dummy_head.next
        
        while(fast and fast.next):
            fast = fast.next
            if k <= 0:
                slow = slow.next
            k -= 1
        
        fast.next = dummy_head.next
        temp = slow.next
        slow.next = None
        
        return temp
        