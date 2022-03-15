class Solution {
public:
    struct compare{
        
        bool operator()(vector<int> left, vector<int> right){
            if(left[0] == right[0]){
                return left[1] > right[1];
            } else{
                return left[0] > right[0];
            }
        }
        
    };
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        priority_queue<vector<int>, vector<vector<int>>, compare> pq; //size, index
        
        for(int i = 0; i < mat.size(); i++){
            int counter = 0;
            for(int j=0; j < mat[i].size(); j++){
                if (mat[i][j]){
                    counter += 1;
                } else{
                    break;
                }   
            }
            
            pq.push(vector<int>{counter, i});
        }
        
        vector<int> ans;
        
        for(; k > 0; k--){
            ans.push_back(pq.top()[1]);
            pq.pop();
        }
        
        
        
        return ans;
    }
};