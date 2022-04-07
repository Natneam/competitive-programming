# LINK TO THE PROBLEM => https://leetcode.com/problems/map-of-highest-peak/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # finding the water cells
        queue = deque()
        heights = []
        
        for row in range(len(isWater)):
            rowList = []
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    rowList.append(0)
                    queue.append((row,col))       
                else:
                    rowList.append(-1)
            heights.append(rowList)
        
        def ingrid(row,col):
            return (0 <= row < len(heights) and 0 <= col < len(heights[0]))
        
        while queue:
            row, col = queue.popleft()
            
            #checking four adjecent spots
            if ingrid(row - 1, col) and heights[row-1][col] == -1:
                heights[row - 1][col] = heights[row][col] + 1 
                queue.append((row - 1, col))
            if ingrid(row, col - 1) and heights[row][col - 1] == -1:
                heights[row][col - 1] = heights[row][col] + 1 
                queue.append((row, col - 1))
            if ingrid(row + 1, col) and heights[row + 1][col] == -1:
                heights[row + 1][col] = heights[row][col] + 1 
                queue.append((row + 1, col))
            if ingrid(row, col + 1) and heights[row][col + 1] == -1:
                heights[row][col + 1] = heights[row][col] + 1
                queue.append((row, col + 1))
        
        
        return heights 