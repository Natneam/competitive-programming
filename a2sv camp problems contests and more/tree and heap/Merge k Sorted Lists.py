# LINK TO THE PROBLEM => https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sortingArr = [0 for _ in range(2 * 10**4 + 1)]
        
        for i in lists:
            currNode = i
            while currNode:
                sortingArr[currNode.val+(10**4)] += 1
                currNode = currNode.next
        
        output = None
        curr = output
        for i in range(len(sortingArr)):
            for j in range(sortingArr[i]):
                if not output:
                    output = ListNode(i - 10**4)
                    curr = output
                    continue
                curr.next = ListNode(i - 10**4)
                curr = curr.next
        return output