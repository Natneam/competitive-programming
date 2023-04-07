class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_graph = defaultdict(list)
        indegree = [0]*len(graph)
        
        # flip the graph
        for i in range(len(graph)):
            for k in graph[i]:
                new_graph[k].append(i)
                indegree[i] += 1
                
        res = []
        queue = deque()
        
        for i in range(len(indegree)):
            if not indegree[i]:
                queue.append(i)
        
        # topological sort
        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            for node in new_graph[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        return sorted(res)
            