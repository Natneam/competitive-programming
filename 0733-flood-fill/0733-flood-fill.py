class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        image[sr][sc] = color
        self.dfs(image, sr, sc, color, original_color, set())
        return image
        
    
    def dfs(self, image, i, j, color, original_color, visited):
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.isvalid(image, i + x, j + y, original_color, visited):
                visited.add((i + x, j + y))
                image[i + x][j + y] = color
                self.dfs(image, i + x, j + y, color, original_color, visited)
        
    def isvalid(self, image, i, j, color, visited):
        return 0 <= i < len(image) and 0 <= j < len(image[0]) and (i, j) not in visited and image[i][j] == color
            