class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(arr, start, end):
            if start > end:
                return float('-inf')
            
            mid = start + (end - start) // 2
            left_sum = 0
            right_sum = 0
            
            # find the maximum left subbary sum which includes the element at [mid - 1]
            curr_sum = 0
            
            for i in range(mid - 1, start - 1, -1):
                curr_sum += nums[i]
                left_sum = max(left_sum, curr_sum)           
            
            # find the maximum right subbary sum whihc includes the element at [mid + 1]
            curr_sum = 0
            
            for i in range(mid+1, end+1):
                curr_sum += nums[i]
                right_sum = max(right_sum, curr_sum)
            
            
            return max(right_sum + nums[mid] + left_sum, solve(arr, mid+1, end), solve(arr, start, mid-1))
        return solve(nums, 0, len(nums) - 1)