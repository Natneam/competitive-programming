# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #find lengths
        temp1 = headA
        temp2 = headB
        
        len1 = 0
        while temp1:
            temp1 = temp1.next
            len1 += 1
        len2 = 0
        while temp2:
            temp2 = temp2.next
            len2 += 1

        while len1 > len2:
            headA = headA.next
            len1 -= 1
        
        while len2 > len1:
            headB = headB.next
            len2 -= 1

        
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        
        
        
        