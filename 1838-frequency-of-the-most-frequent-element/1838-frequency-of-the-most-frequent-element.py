class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        ans = 1
        
        for end in range(1, len(nums)):
            k -= (nums[end] - nums[end-1]) * (end - start)
            
            while k < 0:
                k += nums[end] - nums[start]
                start += 1
            ans = max(ans, end - start + 1)
            
        return ans