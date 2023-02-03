class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        
        i = 0
        for j in range(len(path)):
            if path[j] != "":
                path[i] = path[j]
                i += 1
        path = path[:i]
        
        stack = []
        
        for p in path:
            if p == ".":
                pass
            elif p == "..":
                if stack: stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)