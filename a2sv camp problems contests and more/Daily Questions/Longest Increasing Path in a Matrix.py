# LINK TO THE PROBLEM => https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        longestLength = 0
        dp = dict()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row, col) not in dp:
                    val = self.dfs(matrix, row,col, dp)
                    longestLength = max(longestLength, val)
                    dp[(row,col)] = val
                else:
                    longestLength = max(longestLength, dp[(row,col)])
        return longestLength
        
        
    def dfs(self, matrix, row, col, dp):
        if (row, col) in dp:
            return dp[(row,col)]
        
        val1,val2,val3,val4 = 0,0,0,0
        
        if self.inmatrix(matrix, row-1,col) and matrix[row-1][col] > matrix[row][col]:
            val1 = self.dfs(matrix, row-1, col, dp)
            dp[(row-1, col)] = val1
        if self.inmatrix(matrix, row+1,col) and matrix[row+1][col] > matrix[row][col]:
            val2 = self.dfs(matrix, row+1, col, dp)
            dp[(row+1, col)] = val2
        if self.inmatrix(matrix, row,col-1) and matrix[row][col-1] > matrix[row][col]:
            val3 = self.dfs(matrix, row, col-1, dp)
            dp[(row, col-1)] = val3
        if self.inmatrix(matrix, row,col+1) and matrix[row][col+1] > matrix[row][col]:
            val4 = self.dfs(matrix, row, col+1, dp)
            dp[(row, col+1)] = val4
        
        return max(val1,val2,val3,val4) + 1
        
    def inmatrix(self, matrix, row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
