# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return self.find_intersection(head, slow)    
        return None
    
    def find_intersection(self, head, pointer):
        while head:
            if pointer == head:
                return head
            
            head = head.next
            pointer = pointer.next
    