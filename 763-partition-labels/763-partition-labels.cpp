class Solution {
public:
    int find(int i, char c ,string* s){
        int ans = i;
        for(;i < s->size(); i++){
            if ((*s)[i] == c){
                ans = i;
            }
        }
        
        return ans + 1;
    }
    
    vector<int> partitionLabels(string s) {
        int start = 0;
        int end = 1;
        vector<int> ans;
        
        while(end <= s.size()){
            for(int i = start; i < end; i++){
                end = max(end, find(i, s[i], &s));
            }
            ans.push_back(end - start);
            start = end;
            end += 1;
        }
        
        return ans;
    }
};