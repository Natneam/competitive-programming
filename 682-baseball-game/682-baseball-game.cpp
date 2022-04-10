class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> stack{};
        
        for(auto op : ops){
            if(op == "+"){
                int prev = stack.back();
                stack.pop_back();
                int newVal = prev + stack.back();
                stack.push_back(prev);
                stack.push_back(newVal);
            } else if( op == "D"){
                stack.push_back(stack.back() * 2);
            } else if (op == "C"){
                stack.pop_back();
            } else{
                stack.push_back(stoi(op));
            }
        }
        
        int sum{};
        
        for(auto i : stack){
            sum+=i;
        }
        
        return sum;
        
    }
};