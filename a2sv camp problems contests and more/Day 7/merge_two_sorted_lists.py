# LINK TO THE PROBLEM => https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr_head_1 = l1
        curr_head_2 = l2
        sorted_list = None
        indicator = None
        
        while True:
            # handling edge cases
            if curr_head_1 == None and curr_head_2 == None:
                return sorted_list
            elif curr_head_1 != None and curr_head_2 == None:
                while curr_head_1 != None:
                    if sorted_list == None:
                        sorted_list = ListNode(curr_head_1.val)
                        indicator = sorted_list
                    else:
                        indicator.next = ListNode(curr_head_1.val)
                        indicator = indicator.next
                    curr_head_1 = curr_head_1.next
                return sorted_list
            elif curr_head_2 != None and curr_head_1 == None:
                while curr_head_2 != None:
                    if sorted_list == None:
                        sorted_list = ListNode(curr_head_2.val)
                        indicator = sorted_list
                    else:
                        indicator.next = ListNode(curr_head_2.val)
                        indicator = indicator.next
                    curr_head_2 = curr_head_2.next
                return sorted_list
            
            # merging normal non-zero length linked lists
            if curr_head_1.val > curr_head_2.val:
                if sorted_list == None:
                    sorted_list = ListNode(curr_head_2.val)
                    indicator = sorted_list
                else:
                    indicator.next = ListNode(curr_head_2.val)
                    indicator = indicator.next
                curr_head_2 = curr_head_2.next
            elif curr_head_1.val <= curr_head_2.val:
                if sorted_list == None:
                    sorted_list = ListNode(curr_head_1.val)
                    indicator = sorted_list
                    print(indicator)
                else:
                    indicator.next = ListNode(curr_head_1.val)
                    indicator = indicator.next
                curr_head_1 = curr_head_1.next
                
            