class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -float('inf')
        previous = -float('inf')
        
        for num in nums:
            if num + previous > num:
                previous = num + previous
            else:
                previous = num
            maximum = max(maximum, previous)
        
        return maximum