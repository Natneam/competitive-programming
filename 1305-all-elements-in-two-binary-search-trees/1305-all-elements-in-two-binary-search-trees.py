# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, arr):
            if not root:
                return
            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
            
        
        arr1 = []
        arr2 = []
        dfs(root1, arr1)
        dfs(root2, arr2)
        
        ans = []
        i, j = 0, 0
        while i < len(arr1) or j < len(arr2):
            if i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    ans.append(arr1[i])
                    i += 1
                else:
                    ans.append(arr2[j])
                    j += 1
            elif i < len(arr1):
                ans.append(arr1[i])
                i += 1
            else:
                ans.append(arr2[j])
                j += 1
            
        return ans