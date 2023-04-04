class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # build graph
        graph = defaultdict(list)
        indegree = [0]*n
        
        for relation in relations:
            graph[relation[0]].append(relation[1])
            indegree[relation[1] - 1] += 1
        
        # topological sort layer by layer
        queue = deque()
        ages = [0]*n
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                ages[i] = time[i]
                queue.append(i + 1)
        
        while queue:
            curr = queue.popleft()

            for node in graph[curr]:
                ages[node - 1] = max(ages[node - 1], ages[curr - 1] + time[node - 1]) 
                indegree[node - 1] -= 1
                if indegree[node - 1] == 0:
                    queue.append(node)
        
        return max(ages)