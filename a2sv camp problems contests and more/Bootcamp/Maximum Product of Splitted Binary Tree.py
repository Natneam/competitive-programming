# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        memo = dict()
        totalSum = self.nodeSum(root, memo)
        maximumProduct = 0
        queue = deque()
        queue.append(root)
        while queue:
            currNode = queue.popleft()
            if currNode:
                queue.append(currNode.right)
                queue.append(currNode.left)
                maximumProduct = max(maximumProduct, self.findProduct(currNode.right,memo, totalSum), self.findProduct(currNode.left,memo, totalSum))
        return maximumProduct %  (10**9 + 7)
        
                
        
    def findProduct(self, node, memo, totalSum):
        sumOfNodes = self.nodeSum(node, memo) 
        return sumOfNodes*(totalSum - sumOfNodes)
        
        
    def nodeSum(self, node, memo):
        if not node:
            return 0
        else:
            if node in memo.keys():
                return memo[node]
            memo[node] = node.val + self.nodeSum(node.right, memo) + self.nodeSum(node.left, memo)
            return memo[node]
