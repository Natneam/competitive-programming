class Solution {
public:
    vector<pair<int, int>> dirs = {{-1, 1}, {0, 1}, {1, 1}, {-1, 0}, {1, 0}, {-1, -1}, {0, -1}, {1, -1}};
    void gameOfLife(vector<vector<int>>& board) {
        for(int i{}; i < board.size(); i++){
            for(int j{}; j < board[i].size(); j++){
                int arr[2] = {0, 0};
                for(auto dir : dirs){
                    int new_i{i + dir.first};
                    int new_j{j + dir.second};
                    
                    if( 0 <= new_i && new_i < board.size() && 0 <= new_j && new_j < board[0].size()){
                        arr[(1 & board[new_i][new_j])] += 1;
                    }
                }
                
                if( board[i][j] == 1){
                    if( arr[1] == 2 or arr[1] == 3) board[i][j] = 3;
                } else if(arr[1] == 3) board[i][j] = 2;
            }
        }
        for(int i{}; i < board.size(); i++){
            for(int j{}; j < board[i].size(); j++){
                board[i][j] = board[i][j] >> 1;  
            }
        }
    }
};