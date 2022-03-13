class Solution {
public:
    int findMin(vector<int>& nums) {
        int start = 0;
        int end = nums.size() - 1;
        
        int smallest = nums[0];
        int mid;
        
        while(start <= end){
            mid = start + (end - start) / 2;
            
            if(nums[start] <= nums[mid]){
                smallest = min(smallest, nums[start]);
                start = mid + 1;
            } else {
                smallest = min(smallest, nums[mid]);
                end = mid - 1;
            }
        }
        
        return smallest;
        
    }
};