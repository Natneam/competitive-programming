# LINK TO THE PROBLEM => https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[i-1])
            postfix.append(nums[len(nums)-i-1] + postfix[i-1])
        
        for i in range(len(nums)):
            if postfix[len(nums) - 1 - i] == prefix[i]:
                return i
        return -1