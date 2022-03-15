class Solution {
public:
    int maxProduct(vector<int>& nums) {
        priority_queue<int> q;
        
        for(auto num : nums){
            q.push(num);
        }
        
        int num1 = q.top();
        q.pop();
        int num2 = q.top();
        
        return (num1 - 1) * (num2 - 1);
    }
};