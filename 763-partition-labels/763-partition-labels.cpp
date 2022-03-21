class Solution {
public:
    vector<int> partitionLabels(string s) {
        unordered_map<char, int> lastOf;
        int start = 0;
        int end = 1;
        vector<int> ans;
        
        for(int i = 0; i < s.size(); i++) lastOf[s[i]] = i;
        
        while(end <= s.size()){
            for(int i = start; i < end; i++){
                end = max(end, lastOf[s[i]] + 1);
            }
            ans.push_back(end - start);
            start = end;
            end += 1;
        }
        
        return ans;
    }
};