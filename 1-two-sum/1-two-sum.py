class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = {}
        
        for i in range(len(nums)):
            if target - nums[i] in s_nums:
                return i, s_nums[target - nums[i]]
            else:
                s_nums[nums[i]] = i
        return -1 # shouldn't reach this point
                