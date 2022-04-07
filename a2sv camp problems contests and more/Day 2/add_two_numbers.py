# LINK TO THE PROBLEM : https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        summation = None
        currentNode = ListNode()
        nextNode = ListNode()
        carry = 0
        count = 0
        next = [l1, l2]
        while True:
            tempSum = next[0].val + next[1].val + carry
            if len(str(tempSum)) == 2:
                carry = int(str(tempSum)[0])
                tempSum = int(str(tempSum)[-1])
            else:
                carry = 0            
            currentNode.val = tempSum
            if next[0].next == None and next[1].next == None:
                if carry != 0:
                    currentNode.next = ListNode(carry)
                else:  
                    currentNode.next = None
            else:
                currentNode.next = nextNode
            if count == 0:
                summation = currentNode
            
            currentNode = currentNode.next
            nextNode = ListNode()

            next[0], next[1] = next[0].next, next[1].next
            if next[0] == None and next[1] == None:
                return summation
            else:
                if next[0] == None:
                    next[0] = ListNode(0)
                elif next[1] == None:
                    next[1] = ListNode(0)
            count += 1

# Input: l1 = [2,4,3], l2 = [5,6,4]
# l1 = ListNode(2)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

# l2 = ListNode(5)
# l2.next = ListNode(6)
# l2.next.next = ListNode(4)

# x = Solution.addTwoNumbers(Solution,l1,l2)
# print(f'summation: {x.val}')
# print(f'summation.next: {x.next.val}')
# print(f'summation.next.next: {x.next.next.val}')
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
