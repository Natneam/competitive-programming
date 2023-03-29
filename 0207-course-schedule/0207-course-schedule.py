class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph
        graph = defaultdict(list)
        for p in prerequisites:
            graph[p[1]].append(p[0])
        
        indegree = [0]*numCourses
        for k in graph:
            for val in graph[k]:
                indegree[val] += 1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            
            for key in graph[curr]:
                indegree[key] -= 1
                if indegree[key] == 0:
                    queue.append(key)
        
        return all([x == 0 for x in indegree])