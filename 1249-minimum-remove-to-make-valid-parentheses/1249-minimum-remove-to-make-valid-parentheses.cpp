class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> stk;
        unordered_set<int> to_remove;
        
        for(int i=0; i < s.size() ;i++){
            if(s[i] == '('){
                stk.push(i);
            } else if (s[i] == ')'){
                if (stk.size() > 0){
                    stk.pop();
                } else{
                    to_remove.insert(i);
                }
            }
        }
        
        while(stk.size() > 0){
            to_remove.insert(stk.top());
            stk.pop();
        }
        
        string ans;
        
        for(int i=0; i < s.size(); i++){
            if(to_remove.find(i) == to_remove.end()) ans.push_back(s[i]);
        }
        
        return ans;
        
    }
};