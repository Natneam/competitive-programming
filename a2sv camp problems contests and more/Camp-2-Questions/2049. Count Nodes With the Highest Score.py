class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        tree = defaultdict(list)
        memo = {}
        
        #tree construction
        for i in range(len(parents)):
            if parents[i] == -1:
                continue
            tree[parents[i]].append(i)
        
        self.dfs(tree, 0, memo)
        
        node_values = []
        
        for i in range(len(parents)):
            val = 1
            if memo[i][1] != 0:
                val *= memo[i][1]
            if memo[i][2] != 0:
                val *= memo[i][2]

            if memo[0][0] - memo[i][0] > 0:
                val *= memo[0][0] - memo[i][0]
                
            node_values.append(val)
        return node_values.count(max(node_values))
        
    def dfs(self, tree, start, memo):
        if start in memo:
            return memo[start]
        
        child_vals = [0, 0]
        
        for i in range(len(tree[start])):
            value = self.dfs(tree, tree[start][i], memo)
            child_vals[i] = value[0]
        
        # sum of all the subordinate nodes including itself, sum of right subordinate nodes, sum of left subordinate nodes
        memo[start] = child_vals[0] + child_vals[1] + 1, child_vals[0], child_vals[1]
        return memo[start]