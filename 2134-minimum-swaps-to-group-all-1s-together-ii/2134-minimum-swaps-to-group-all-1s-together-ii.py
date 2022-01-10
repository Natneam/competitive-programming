class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        count all ones 
        
        see all the window with the size the number of ones and count zeros and take the minimum,
        consider the wrap around
        
        """
        ones = nums.count(1)
        window = [0, 0]
        
        for i in range(ones):
            window[nums[i]] += 1
        
        minimum = window[0]
        
        for i in range(ones, len(nums)):
            window[nums[i - ones]] -= 1
            window[nums[i]] += 1
            
            minimum = min(minimum, window[0])
            
        for i in range(ones):
            window[nums[len(nums) - ones + i]] -= 1
            window[nums[i]] += 1
            minimum = min(minimum, window[0])
        
        return minimum
        
        
            
            