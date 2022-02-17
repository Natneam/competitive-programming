class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #bfs
        queue = deque([(sr, sc)])
        
        original_color = image[sr][sc]
        
        if newColor == original_color:
            return image
        
        def is_valid(i, j):
            row = len(image)
            col = len(image[0])
            return 0 <= i < row and 0 <= j < col and image[x][y] == original_color
        
        while queue:
            index_x, index_y = queue.popleft()
            
            image[index_x][index_y] = newColor
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for dir_x, dir_y in directions:
                x, y = index_x + dir_x, index_y + dir_y
                if is_valid(x, y):
                    queue.append((x, y))
        return image