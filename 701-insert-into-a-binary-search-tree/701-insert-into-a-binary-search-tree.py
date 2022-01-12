# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        def insert(node, val):
            if node.val < val:
                if node.right:
                    insert(node.right, val)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    insert(node.left, val)
                else:
                    node.left = TreeNode(val)
        insert(root, val)
        return root