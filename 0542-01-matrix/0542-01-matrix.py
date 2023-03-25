class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        queue = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
        self.bfs(mat, res, deque(queue))
        return res
    
    def bfs(self, mat, res, queue):
        visited = set(list(queue))
        temp_queue = []
        level = 0
        
        while queue or temp_queue:
            if not len(queue):
                level += 1
                queue = deque(temp_queue)
                temp_queue = []
            
            x, y = queue.popleft()
            visited.add((x, y))
            if mat[x][y] == 1:
                if res[x][y] == 0: res[x][y] = level
                else: res[x][y] = min(res[x][y], level)
            
            for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + a, y + b
                if self.isvalid(mat, new_x, new_y, visited):
                    temp_queue.append((new_x, new_y))
                
    def isvalid(self, mat, x, y, visited):
        return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and (x, y) not in visited