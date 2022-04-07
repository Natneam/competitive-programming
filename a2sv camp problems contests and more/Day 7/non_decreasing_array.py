# LINK TO THE PROBLEM => https://leetcode.com/problems/non-decreasing-array/
class Solution:
    def checkPossibility(self, nums):
        modifiedElements = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                modifiedElements += 1
                try:
                    if (i-1 >= 0) and nums[i-1] > nums[i+1] and nums[i] > nums[i+2]:
                        return False
                except:
                    pass
                
            if modifiedElements > 1:
                return False
        return True