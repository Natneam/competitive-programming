class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        temp_queue = []
        res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue or temp_queue:
            if not queue:
                queue = deque(temp_queue)
                temp_queue = []
                res += 1
            
            x, y = queue.popleft()
            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + i, y + j
                if self.isvalid(grid, new_x, new_y):
                    grid[new_x][new_y] = 2
                    temp_queue.append((new_x, new_y))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
    
    def isvalid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1
