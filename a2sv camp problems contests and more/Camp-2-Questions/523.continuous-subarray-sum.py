#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i-1])
        
        reminders = [x % k for x in prefix_sum]
        
        visited = set()
        prev = 0        
        
        for i in reminders:
            if i in visited:
                return True
            visited.add(prev)
            prev = i
        
        return False
        
# @lc code=end

