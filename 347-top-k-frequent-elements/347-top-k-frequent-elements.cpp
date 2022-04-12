class Solution {
public:
    struct cmp{
        bool operator()(pair<int, int> a, pair<int, int> b){
            return a.first < b.first;
        }
    };
    
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq{};
        
        for(auto num : nums){
            freq[num]++;
        }
        
        priority_queue<pair<int, int> , vector<pair<int, int>>, cmp> pq{};
        vector<int> ans{};
        
        for(auto item : freq){
            pq.push(pair<int, int>{item.second, item.first});
        }
        
        for(;k>0;k--){
            // cout << pq.top().first << " ";
            ans.push_back(pq.top().second);
            pq.pop();
        }
        
        return ans;
    }
};