# LINK TO THE PROBLEM =>  https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        indexOfMax = nums.index(max(nums))
        node = TreeNode(nums[indexOfMax])
        node.left = self.constructMaximumBinaryTree(nums[:indexOfMax])
        node.right = self.constructMaximumBinaryTree(nums[indexOfMax+1:])
        return node

# using indices
# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         return self._helper(nums, 0, len(nums)-1)
        
#     def _helper(self, nums, start, end):
#         if start > end:
#             return None

#         maxValue = -1
#         indexOfMax = 0
#         tempStart = start
#         while tempStart <= end:
#             if nums[tempStart] > maxValue:
#                 maxValue = nums[tempStart]
#                 indexOfMax = tempStart
#             tempStart += 1         
        
#         node = TreeNode(nums[indexOfMax])
#         node.left = self._helper(nums, start, indexOfMax-1)
#         node.right = self._helper(nums, indexOfMax+1, end)
#         return node