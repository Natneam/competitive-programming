class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == "1":
                    self.dfs(grid, visited, i, j)
                    res += 1
        return res
                    
    def dfs(self, grid, visited, i, j):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited.add((i, j))
        
        for x, y in directions:
            next_i, next_j = i + x, j + y
            self.isvalid(next_i, next_j, grid, visited) and self.dfs(grid, visited, next_i, next_j)
    
    def isvalid(self, i, j, grid, visited):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and \
                (i, j) not in visited and grid[i][j] == "1"