class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        
        values = set()
        for v in graph.values():
            for l in v:
                values.add(l)
            
        return list(set(range(0, n)) - values)
        