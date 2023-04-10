class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # build graph
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        
        memo = {}
        def dfs(a , b):
            if (a, b) in memo:
                return memo[(a, b)]
            
            if a == b:
                return True
            
            if a in graph:
                for item in graph[a]:
                    if dfs(item, b):
                        memo[(a, b)] = True
                        return True
            memo[(a, b)] = False
            return False
        
        res = []
        for i, j in queries:
            res.append(dfs(i, j))
        
        return res