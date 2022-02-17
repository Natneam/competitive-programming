class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """
        m * n -> count the negative numbers in each row
        m * log(n) -> find the first occurance of negative number using binary searhc in each row
        m + n start from the end of the first row and advance the row index until you the firs negative number, increament the row number
        """
        # Approch 1
        # ans = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] < 0:
        #             ans += 1
        # return ans
        
        # Approch 2
        # def bin_search(arr):
        #     start = 0
        #     end = len(arr) - 1
        #     index = len(arr) 

        #     while start <= end:
        #         mid = start + (end - start)//2
        #         if arr[mid] < 0:
        #             index = min(index, mid)
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        #     return index

        # ans = 0
        # for i in range(len(grid)):
        #     ans += len(grid[i]) - bin_search(grid[i])
        # return ans
        
        #Approch 3
        row, col = 0, len(grid[0])
        ans = 0
        
        while row < len(grid):
            while col > 0 and grid[row][col - 1] < 0:
                col -= 1
            ans += len(grid[0]) - col
            
            row += 1
        return ans
            
            