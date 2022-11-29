class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        summation = 0
        start = 0
        ans = 0
        
        for end in range(len(nums)):
            summation += nums[end]
            
            if(end - start + 1 == k):
                if(summation / k >= threshold):
                    ans += 1
                
                summation -= nums[start]
                start += 1
        return ans