class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # level-order BFS with state (vertex, path_mask)
        n = len(graph)
        goal = (1 << n) - 1
        level = [(u, 1 << u) for u in range(n)]
        seen = set(level)
        length = 0
        
        while True:
            nxt = []
            for u, mask in level:
                if mask == goal:
                    return length
                for v in graph[u]:
                    n_tup = (v, mask | (1 << v))
                    if n_tup not in seen:
                        nxt.append(n_tup)
                        seen.add(n_tup)
            level = nxt
            length += 1