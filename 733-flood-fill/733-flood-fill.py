class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #bfs
        # queue = deque([(sr, sc)])

        # original_color = image[sr][sc]

        # if newColor == original_color:
        #     return image

        # def is_valid(i, j):
        #     row = len(image)
        #     col = len(image[0])
        #     return 0 <= i < row and 0 <= j < col and image[i][j] == original_color

        # while queue:
        #     index_x, index_y = queue.popleft()

        #     image[index_x][index_y] = newColor

        #     directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        #     for dir_x, dir_y in directions:
        #         x, y = index_x + dir_x, index_y + dir_y
        #         if is_valid(x, y):
        #             queue.append((x, y))
        # return image
        
        #dfs
        
        def is_valid(image, i, j, original_color):
            row = len(image)
            col = len(image[0])
            return 0 <= i < row and 0 <= j < col and image[i][j] == original_color
        
        def dfs(image, visited, indexes, original_color, new_color):
            index_x, index_y =indexes[0], indexes[1]
            image[index_x][index_y] = new_color
            
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            for x, y in directions:
                new_x , new_y = index_x + x, index_y + y
                if is_valid(image, new_x, new_y, original_color) and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    dfs(image, visited, (new_x, new_y), original_color, new_color)
            
        dfs(image, set([(sr, sc)]), (sr, sc), image[sr][sc], newColor)
        return image