# LINK TO THE PROBELM => https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        s = set()
        numRow = len(image)      
        numCol = len(image[0])
        return self._helper(image, sr, sc, newColor, s, numRow, numCol)
        
        
    def _helper(self, image, sr, sc, newColor, visited, numRow, numCol):
        if 0 <= sr < numRow and 0 <= sc < numCol and (sr,sc) not in visited:
            visited.add((sr, sc))
            if sr > 0 and image[sr-1][sc] == image[sr][sc]:
                self._helper(image, sr-1, sc, newColor, visited, numRow, numCol)
            if sr < numRow-1 and image[sr+1][sc] == image[sr][sc]:
                self._helper(image, sr+1, sc, newColor, visited, numRow, numCol)
            if sc > 0 and image[sr][sc-1] == image[sr][sc]:
                self._helper(image, sr, sc-1, newColor, visited, numRow, numCol)
            if sc < numCol-1 and image[sr][sc+1] == image[sr][sc]:
                self._helper(image, sr, sc+1, newColor, visited, numRow, numCol)
            image[sr][sc] = newColor
        return image