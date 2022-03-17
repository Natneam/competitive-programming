class Solution {
public:
    int scoreOfParentheses(string s) {
        stack<string> stk;
        int sum = 0;
        
        for(auto i : s){
            if(i == '('){
                stk.push(string(1, i));
            } 
            else{
                if (stk.top() == "("){
                    stk.pop();
                    stk.push("1");
                } else {
                    sum = 0;
                    while(stk.top() != "("){
                        sum += stoi(stk.top());
                        stk.pop();
                    }
                    
                    stk.pop();
                    stk.push(to_string(sum * 2));
                }
            }
        }
        int ans = 0;
        
        while(!stk.empty()) {
            ans += stoi(stk.top());
            stk.pop();
        }
        
        return ans;
    }
};