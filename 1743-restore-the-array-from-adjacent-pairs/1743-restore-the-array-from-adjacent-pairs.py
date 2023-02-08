class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, j in adjacentPairs:
            graph[a].append(j)
            graph[j].append(a)
        
        start = None
        for g in graph:
            if len(graph[g]) == 1:
                start = g
                break
        res = [start]
        visited = set(res)
        
        for _ in range(len(graph) - 1):
            if len(graph[start]) > 1 and graph[start][0] in visited:
                start = graph[start][1]
            else:
                start = graph[start][0]
            visited.add(start)
            res.append(start)
            
        return res