class Solution:
    def simplifyPath(self, path: str) -> str:
        path, i = path.split("/"), 0
        
        for j in range(len(path)):
            if path[j] != "":
                path[i] = path[j]
                i += 1
        
        stack = []
        for p in path[:i]:
            if p == "..":
                if stack: stack.pop()
            elif p not in ["", "."]:
                stack.append(p)
        
        return "/" + "/".join(stack)