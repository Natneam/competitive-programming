class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # build graph and indegree
        graph = defaultdict(list)
        indegree = [0]*len(quiet)
        queue = deque()
        res = []
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
            res.append(i)
        
        while queue:
            curr = queue.popleft()

            for node in graph[curr]:
                if quiet[res[curr]] < quiet[res[node]]:
                    res[node] = res[curr]
                
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        return res