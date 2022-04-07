# LINK TO THE PROBLEM => https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maximum = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == 1:
                    maximum = max(maximum, self.dfs(grid, row, col, visited))
        return maximum
    
    def dfs(self, grid, row, col, visited):
        if not len(grid) > row >= 0 or not len(grid[0]) > col >= 0 or (row, col) in visited or grid[row][col] == 0:
            return 0
        
        visited.add((row, col))
        val = 1
        val += self.dfs(grid, row - 1, col, visited)
        val += self.dfs(grid, row + 1, col, visited)
        val += self.dfs(grid, row, col - 1, visited)
        val += self.dfs(grid, row, col + 1, visited)
        
        return val
                    