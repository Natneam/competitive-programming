//https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int length = nums.size();
        int k;
        for(k = length - 2 ; k >= 0; k -- ){
            if(nums[k] < nums[k+1]) break;
        }
        
        if(k < 0){
            reverse(nums.begin(), nums.end());
        } else{
            for(int l = length - 1; l > k; l--){
                if(nums[k] < nums[l]){
                    swap(nums[k], nums[l]);
                    break;
                }
            }
            reverse(nums.begin() + k + 1, nums.end());
        }
    }
};