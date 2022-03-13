class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> char_map= {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };
        
        stack<char> new_stack;
        
        
        for(auto chr : s){
            if (chr == '(' || chr == '[' || chr == '{'){
                new_stack.push(chr);
            }else{
                
                if(new_stack.empty() || char_map[new_stack.top()] != chr){
                    return false;
                }
                
                new_stack.pop();
            }
        }
        
        if (new_stack.empty()) return true;
        return false;
    }
};