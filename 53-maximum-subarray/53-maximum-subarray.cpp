class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ans = nums[0];
        int prev = nums[0];
        
        for(int i = 1; i < nums.size(); i++){
            
            if (nums[i] + prev > nums[i]){
                prev = nums[i] + prev;
            }else{
                prev = nums[i];
            }
            ans = max(ans, prev);   
        }
        return ans;
            
    }
};