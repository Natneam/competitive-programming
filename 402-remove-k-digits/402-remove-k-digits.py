class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        let's keep a monotonic stack, non decreasing
        until k elements removed from the stack keep the stack monotonic
        then concatinate the stack and remove the last remaining k elelemnts from th e stack        
        """
        stack = []
        for i in num:
            while stack and k > 0 and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        
        for i in range(k):
            stack.pop()
            
        ans = str(int("".join(stack))) if stack else "0" 
        
        return ans