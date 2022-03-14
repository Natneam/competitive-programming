class Solution {
public:
    string simplifyPath(string path) {
        vector<string> stk;
        
        for(int i = 1; i < path.size(); i++){
            string curr_name = "";
            
            while(i < path.size() && path[i] != '/'){
                curr_name.push_back(path[i]);
                i++;
            }
            
            if(curr_name == "." || curr_name == "") continue;
            else if (curr_name == ".." && stk.size() > 0) stk.pop_back();
            else if (curr_name != "..") stk.push_back(curr_name);
        }
        
        string ans = "";
        
        for(auto i : stk) ans = ans + "/" + i;
             
        return ans.size() > 0 ? ans : "/";
    }
};