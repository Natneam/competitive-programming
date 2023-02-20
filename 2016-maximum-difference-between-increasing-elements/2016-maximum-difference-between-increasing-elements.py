class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = nums[0]
        res = -1
        for num in nums:
            if num <= curr_min:
                curr_min = num
            else:
                res = max(res, num - curr_min)
        return res