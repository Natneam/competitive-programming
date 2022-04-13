class Solution {
public:
    bool change_direction(vector<vector<int>> ans, vector<int> curr_index, vector<vector<int>> dirs, int dir, int n){
            return (curr_index[0] + dirs[dir][0] < 0 ||  curr_index[0] + dirs[dir][0] >= n || curr_index[1] + dirs[dir][1] < 0 || curr_index[1] + dirs[dir][1] >= n || ans[curr_index[0] + dirs[dir][0]][curr_index[1] + dirs[dir][1]] != 0);
        return true;
    }
    
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans{};
        
        for(int i=0; i < n; i++){
            vector<int> temp{};
            for(int j=0; j < n; j++){
                temp.push_back(0);
            }
            ans.push_back(temp);
        }
        
        
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int dir = 0;
        
        
        vector<int> curr_index = {0, 0};
        
        for(int i=1; i <= n*n; i++){
            ans[curr_index[0]][curr_index[1]] = i;
            
            if(change_direction(ans, curr_index, dirs, dir, n)){
                dir = (dir + 1) % 4;
            }
                        
            curr_index[0] = curr_index[0] + dirs[dir][0];
            curr_index[1] = curr_index[1] + dirs[dir][1];
        }
        
        return ans;
    }
};