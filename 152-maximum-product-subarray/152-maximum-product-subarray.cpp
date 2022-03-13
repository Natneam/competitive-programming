class Solution {
public:
    vector<int> find_min_max(vector<int> nums){
        int minimum = nums[0];
        int maximum = nums[0];
        
        for(int i=1; i < nums.size(); i++){
            minimum = min(minimum, nums[i]);
            maximum = max(maximum, nums[i]);
        }
        
        return { minimum, maximum};
    }
    
    int maxProduct(vector<int>& nums) {
        vector<int> min_max = {nums[0], nums[0]};   // prev_min, prev_max
        int ans = nums[0];
        
        for(int i=1; i < nums.size(); i++){
            
            vector<int> temp = {min_max[0] * nums[i], min_max[1] * nums[i], nums[i]};
            
            min_max = find_min_max(temp);
            
            ans = max({ans, min_max[0], min_max[1]});
        }
        
        return ans;
    }
};