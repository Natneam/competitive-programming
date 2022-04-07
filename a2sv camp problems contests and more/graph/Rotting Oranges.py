# LINK TO THE PROBLEM => https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenOranges = deque()
        time = 0
        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottenOranges.append((row, col, time))
        while rottenOranges:
            orange = rottenOranges.popleft()
            x, y = orange[0], orange[1]
            
            time = max(orange[2], time)
            
            if self.ingrid(x+1, y, grid) and grid[x+1][y] == 1:
                grid[x+1][y] = 2
                rottenOranges.append((x+1, y, orange[2]+1))
            if self.ingrid(x-1, y, grid) and grid[x-1][y] == 1:
                grid[x-1][y] = 2
                rottenOranges.append((x-1, y, orange[2]+1))
            if self.ingrid(x, y+1, grid) and grid[x][y+1] == 1:
                grid[x][y+1] = 2
                rottenOranges.append((x, y+1, orange[2]+1))
            if self.ingrid(x, y-1, grid) and grid[x][y-1] == 1:
                grid[x][y-1] = 2
                rottenOranges.append((x, y-1, orange[2]+1))
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return time
    
    def ingrid(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        return False
    