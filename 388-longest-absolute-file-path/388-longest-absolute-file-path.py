class Solution:
    def lengthLongestPath(self, i: str) -> int:
        max_length = 0
        path = i.split('\n')
        stack = [(0, -1)] #[(path_length, depth), ...] 
        
        for p in path:
            depth = p.count("\t")
            length = len(p) - depth
            while stack and stack[-1][1] >= depth:
                    stack.pop()
                    
            if '.' in p:
                max_length = max(max_length, length + stack[-1][0])
            else:
                stack.append((stack[-1][0] + length + 1, depth))
        
        return max_length