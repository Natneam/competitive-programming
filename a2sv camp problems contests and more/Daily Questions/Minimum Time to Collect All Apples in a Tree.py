# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # constructing a sophisticated graph(tree)
        tree = defaultdict(set)
        visited = set()
        for edge in edges:
            tree[edge[0]].add(edge[1])
            tree[edge[1]].add(edge[0])
        
        if not len(hasApple):
            return 0
        return self.dfs(tree, hasApple, 0, visited)
    
    def dfs(self, tree, hasApple, node, visited):
        if node in visited or (not tree[node] and hasApple[node] == False):
            return 0
        if not tree[node] and hasApple[node] == True:
            return 2
        
        visited.add(node)
        val = 0
        for adjNode in tree[node]:
            val += self.dfs(tree, hasApple, adjNode, visited)
        
        if (val == 0 and not hasApple[node]) or node == 0:
            return val
        return val + 2
