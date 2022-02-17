class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        count = 0
        ans = 0
        
        for end in range(len(nums)):
            count += 0 if nums[end] == 1 else 1
            
            while count > 1:                
                if nums[start] == 0:
                    count -= 1
                start +=1
            
            ans = max(ans, end - start + 1)
            
        return ans - 1