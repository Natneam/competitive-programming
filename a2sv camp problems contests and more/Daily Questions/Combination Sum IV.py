# LINK TO THE PROBLEM => https://leetcode.com/problems/combination-sum-iv/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0:1}
        return self.helper(nums, target, dp)
        
    def helper(self, nums, target, dp):
        val = 0
        
        if target in dp.keys():
            return dp[target]
        
        for item in nums:
            if target - item >= 0:
                val += self.helper(nums, target-item, dp)
        
        dp[target] = val
        return val