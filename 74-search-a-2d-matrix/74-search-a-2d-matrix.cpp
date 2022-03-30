class Solution {
public:
    bool searchRow(vector<vector<int>>& matrix, int row, int target){
        int start{0};
        int end = matrix[row].size() - 1;
        int mid {};

        while(start <= end){
            mid = start + (end - start) / 2;
            if(matrix[row][mid] == target) return true;
            else if(matrix[row][mid] < target) start = mid + 1;
            else end = mid - 1;
        }
        
        return false;
    }
    
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        //nlog(m) - binary search each row
        for(int i=0; i < matrix.size(); i++){
            if(searchRow(matrix, i, target)) return true;
        }
        return false;
    }
};