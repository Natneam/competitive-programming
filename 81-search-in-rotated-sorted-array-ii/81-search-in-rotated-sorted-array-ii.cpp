class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size() - 1;
        int mid{};
        
        while (start <= end){
            mid = start + (end - start) / 2;
            
            if (nums[mid] == target){
                return true;
            }
            
            // cout << nums[start] << " " << nums[mid] << " " << nums[end] << endl;
            // cout << start << " " << mid << " " << end << endl;
            
            if (nums[start] < nums[mid]){
                if(nums[start] <= target and target < nums[mid]){
                    end = mid - 1;
                } else{
                    start = mid + 1;
                }
            } else if (nums[start] > nums[mid]) {
                if(nums[mid] < target and target <= nums[end]){
                    start = mid + 1;
                } else{
                    end = mid - 1;
                }
            } else{
                start++;
            }
        }
        
        return false;
        
            
    }
};