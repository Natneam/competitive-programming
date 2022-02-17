class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ["#"]
        
        for a in s:
            if stack[-1] == a:
                while stack[-1] == a:
                    stack.pop()
            else:
                stack.append(a)
        
        return "".join(stack[1:])