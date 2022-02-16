class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
        
        #log the indegree
        indegree = [0]*numCourses
        for node in graph:
            for neighbour in graph[node]:
                indegree[neighbour] += 1
        ans = []
        queue = deque()
        
        for node in range(len(indegree)):
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return ans if all([x==0 for x in indegree]) else []