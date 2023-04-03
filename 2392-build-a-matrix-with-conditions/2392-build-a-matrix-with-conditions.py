class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row = self.findOrder(k, rowConditions)
        col = self.findOrder(k, colConditions)
        
        if len(row) < k or len(col) < k: 
            return []
        
        res = []
        for i in range(k):
            r = []
            for j in range(k):
                if row[i] == col[j]:
                    r.append(col[j])
                else:
                    r.append(0)
            res.append(r)
            
        return res
    
    def findOrder(self, k, conditions):
        # build graph
        graph = defaultdict(list)
        for start, end in conditions:
            graph[start].append(end)
        # find the indegree
        indegree = [0]*k
        for key in graph:
            for val in graph[key]:
                indegree[val - 1] += 1
        
        # topological sort
        queue = deque()
        res = []
        for i in range(len(indegree)):
            if indegree[i] == 0: queue.append(i + 1)
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for node in graph[curr]:
                indegree[node - 1] -= 1
                if indegree[node - 1] == 0:
                    queue.append(node)
        
        return res
        