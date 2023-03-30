class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        # count the indegree of each node
        indegree = [0]*numCourses
        
        for key in graph:
            for val in graph[key]:
                indegree[val] += 1
                
        # put all nodes with indegree 0 to the queue
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        # do bfs while recording the curr element poped from the queue
        res = []
        while queue:
            curr = queue.popleft()
            res.append(curr)
            
            for node in graph[curr]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
        
        return res if all([x == 0 for x in indegree]) else []