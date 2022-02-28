class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ans = []
        _range = [nums[0], 0]
        nums.append(nums[-1] + 10)  #padding
        
        for i in range(1, len(nums)):
            if nums[i] - 1 != nums[i-1]:
                _range[1] = nums[i-1]
                
                if _range[0] != _range[1]:
                    ans.append(f"{_range[0]}->{_range[1]}")
                else:
                    ans.append(str(_range[0]))
                
                _range = [nums[i], 0]
                
        return ans
        