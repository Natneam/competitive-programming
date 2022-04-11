class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int rowCount = grid.size() - 1;
        int colCount = grid[0].size() - 1;
        int lastElementInRow{};
        int lastElementInCol{};
        
        for(int i=0; i < k; i++){
            //shift the array by one column
            lastElementInCol = grid[rowCount][colCount]; 
            for(int row=rowCount;  row >= 0; row--){
                lastElementInRow = grid[row][colCount];
                for(int col=colCount-1; col >= 0; col--){
                    grid[row][col + 1] = grid[row][col];
                }
                if(row < rowCount) grid[row+1][0] = lastElementInRow;
            }

            grid[0][0] = lastElementInCol;
        }
        
        return grid;
    
    }
    
};