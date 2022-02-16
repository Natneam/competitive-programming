class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        
        indegree = [0]*numCourses
        
        #log the indegree of each element
        for node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1
        queue = deque([])
        
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
                
        return all([x==0 for x in indegree])