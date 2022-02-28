class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        buffer = []
        curr = [nums[0], 0]
        nums.append(nums[-1] + 10)
        
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i-1]:
                curr[1] = nums[i-1]
                buffer.append(curr)
                curr = [nums[i], 0]
        
        ans = []
        for item in buffer:
            if item[0] == item[1]:
                ans.append(str(item[0]))
            else:
                ans.append(f"{item[0]}->{item[1]}")
        return ans
        