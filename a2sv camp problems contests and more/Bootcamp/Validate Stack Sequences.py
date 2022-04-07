# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-112/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pointer = 0
        for i in pushed:
            stack.append(i)
            if i == popped[pointer]:
                while len(stack) != 0 and stack[-1] == popped[pointer]:
                    stack.pop()
                    pointer += 1
        return len(stack) == 0