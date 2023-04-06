class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # build graph
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
        
        res  = [set() for _ in range(n)]
        
        @cache
        def dfs(node, curr):
            if node in graph:
                for child in graph[node]:
                    res[child].add(curr)
                    dfs(child, curr)
                    
        for node in graph:
            dfs(node, node)
        
        return [sorted(list(x)) for x in res]
        
        
    
        