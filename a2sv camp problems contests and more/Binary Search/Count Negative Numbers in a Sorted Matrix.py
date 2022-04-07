# LINK TO THE PROBLEM => https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        currRow, currCol = len(grid) - 1, len(grid[0]) - 1
        count = 0
        
        while currCol >= 0 and grid[currRow][currCol] < 0:
            currCol -= 1
        count += len(grid[0]) - currCol -1
        
        if currCol == len(grid[0]) - 1:
            return count 
        
        currRow -= 1
        currCol += 1
        
        while currRow > -1:
            while currCol < len(grid[0]) and grid[currRow][currCol] >= 0:
                currCol += 1
            count += len(grid[0]) - currCol
            currRow -= 1
        return count