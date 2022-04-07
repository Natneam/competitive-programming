# LINK TO THE PROBLEM => https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        absolutePath =[x for x in path.split("/") if x != '']
        canonicalPath = []
        
        for i in absolutePath:
            if i == "..":
                if len(canonicalPath) != 0:
                    canonicalPath.pop()
            elif i == ".":
                pass
            else:
                canonicalPath.append(i)
        return "/" + "/".join(canonicalPath)