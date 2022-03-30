class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // search the column the to find the largest number which is less than or equals the target
        // then search this row to find the exact target
        
        //search the column
        int start{0};
        int end = matrix.size() - 1;
        int bestSoFar{};
        int mid{};
        
        while(start <= end){
            mid = start + (end - start)/2;
            if(matrix[mid][0] <= target){
                bestSoFar = mid;
                start = mid + 1;
            } else end = mid - 1;
        }
        
        
        //search the row
        
        start = 0;
        end = matrix[bestSoFar].size() - 1;
        mid = 0;
        
        while(start <= end){
            mid = start + (end - start) / 2;
            if(matrix[bestSoFar][mid] == target) return true;
            else if (matrix[bestSoFar][mid] < target) start = mid + 1;
            else end = mid - 1;
        }
        
        return false;
        
    }
};