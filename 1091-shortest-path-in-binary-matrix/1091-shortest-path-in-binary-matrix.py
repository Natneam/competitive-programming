class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #do bfs
        def is_valid(x, y, visited):
            return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] == 0 and (x, y) not in visited
            
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        visited = set()
        queue = deque()
        
        if grid[0][0] == 0:
            queue.append((1, 0, 0))
            visited.add((0, 0))
        
        while queue:
            depth, x, y = queue.popleft()
            if (x, y) == (len(grid) - 1, len(grid) - 1):
                return depth
            
            for d in directions:
                if is_valid(x + d[0], y + d[1], visited):
                    queue.append((depth + 1, x + d[0], y + d[1]))
                    visited.add((x + d[0], y + d[1]))
        return -1 
        
        