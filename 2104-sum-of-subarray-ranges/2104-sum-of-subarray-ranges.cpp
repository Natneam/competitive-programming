class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {
        long long ans = 0;
        for(int i = 0; i < nums.size(); i++){
            int _min = nums[i];
            int _max = nums[i];
            
            for (int j = i+1; j < nums.size(); j++){
                if (nums[j] < _min) _min = nums[j];
                if (nums[j] > _max) _max = nums[j];
                ans += _max - _min;
            }
        }
        
        return ans;
    }
};