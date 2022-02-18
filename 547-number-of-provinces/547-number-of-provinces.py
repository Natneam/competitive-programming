class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #union find
        
        def union(parent, node1, node2):
            p1 = find(parent, node1)
            p2 = find(parent, node2)
            parent[p1] = p2
        
        def find(parent, node):
            curr = node
            while parent[node] != node:
                node = parent[node]

            #path compression
            while parent[curr] != curr:
                temp = curr
                curr = parent[curr]
                parent[temp] = node
            return node
            
        parents = [x for x in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(i+1, len(isConnected[i])):
                if isConnected[i][j] == 1:
                    union(parents, i, j)
        
        #find the ultimate paretns
        parents_set = set()
        for p in parents:
            parents_set.add(find(parents, p))
            
        return len(parents_set)
        