class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, vector<int>> indices;
        
        for(int i = 0; i < s.size(); i++){
            if(indices.find(s[i]) != indices.end()){
                indices[s[i]].push_back(i);
            } else {
                indices[s[i]] = vector<int>{i};
            }
        }
        
        vector<char> stk;
        unordered_set<char> visited;
        
        for(int i = 0; i < s.size(); i++){
            if(visited.find(s[i]) != visited.end()){
                continue;
            } else if (!stk.size() or stk.back() < s[i] or indices[stk.back()].back() <= i){
                stk.push_back(s[i]);
                visited.insert(s[i]);
            } else {
                visited.erase(stk.back());
                stk.pop_back();
                i--;
            }
        }
        
        string ans;
        
        for(auto i : stk){
            ans.push_back(i);
        }
        
        return ans;        
    }
};