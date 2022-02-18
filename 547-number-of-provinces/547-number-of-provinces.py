class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(isConnected, node, visited):    
            for neighbour in range(len(isConnected[node])):
                if isConnected[node][neighbour] == 1 and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(isConnected, neighbour, visited)
        
        visited = set()
        count = 0
        
        for node in range(len(isConnected)):
            if node not in visited:
                dfs(isConnected, node, visited)
                count += 1
        
        return count