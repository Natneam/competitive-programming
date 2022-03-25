class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        vector<pair<int, int>> difference_index;
        int size = costs.size();
        int ans = 0;
        
        for(auto i=0; i < size; i++){
            difference_index.push_back(pair<int, int>{costs[i][0] - costs[i][1], i});
        }
        
        sort(difference_index.begin(), difference_index.end());
        
        for(auto i = 0; i < size; i++){
            if(i <  size/ 2){
                ans += costs[difference_index[i].second][0];
            } else {
                ans += costs[difference_index[i].second][1];
            }
        }
        
        return ans;
        
    }
};