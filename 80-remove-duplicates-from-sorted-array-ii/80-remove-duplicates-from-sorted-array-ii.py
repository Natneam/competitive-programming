class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        start = 0
        
        for num in nums:
            if start < 2 or nums[start - 2] < num:
                nums[start] = num
                start += 1
                
        return start