class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        base case : when it reaches the last row, return the value of the row
        recurence relation : 
            dp[i][j][k][l] = max(dp -> to the three direction for one of the robot) + max(dp -> to the the three direction for one of thr robot)
        
        def (i, j, k, l)
        
        """
        def in_grid(i, k, l):
            if 0 <= i < len(grid) and 0 <= k < len(grid[0]) and 0 <= l < len(grid[0]):
                return True
            return False
        
        @cache
        def cherry_pick(i, k, l):            
            y_s = (-1, 0, 1)
            
            maximum = 0
            
            for y1 in y_s:
                for y2 in y_s:
                    if in_grid(i+1, k + y1, l + y2):
                        maximum = max(maximum, cherry_pick(i+1, k + y1, l + y2))
            if l == k:
                maximum += grid[i][k]
            else:
                maximum = maximum + grid[i][k] + grid[i][l]
            
            return maximum
        
        return cherry_pick(0, 0, len(grid[0])-1)
            
            
            