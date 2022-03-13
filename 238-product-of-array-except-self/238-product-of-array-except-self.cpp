class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ans = {1};
        
        for(int i=0; i < nums.size() - 1; i++) ans.push_back(ans[i] * nums[i]);
        
        for(int i=nums.size() - 2; i >= 0; i--){
                ans[i] = ans[i] * nums[i + 1];
                nums[i] = nums[i] * nums[i + 1];
        }
        
        return ans;
        
    }
};