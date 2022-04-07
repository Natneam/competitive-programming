# LINK TO THE PROBLEM => https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] == nums[j]:
                    output += 1
        return output

