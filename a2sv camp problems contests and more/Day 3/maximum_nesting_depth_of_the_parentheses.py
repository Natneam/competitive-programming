# LINK TO THE PROBLEM => https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        depth = 0
        for i in s:
            if i == '(':
                stack.append(i)
                if len(stack) > depth:
                    depth = len(stack)
            elif i == ')':
                stack.pop()
        return depth