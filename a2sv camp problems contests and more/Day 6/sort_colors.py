# LINK TO THE PROBLEM => https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        lastIndex = len(nums)-1
        firstIndex = 0
        while current <= lastIndex:
            if nums[current] == 0:
                nums[current], nums[firstIndex] = nums[firstIndex], nums[current]
                current += 1
                firstIndex += 1
            elif nums[current] == 2:
                # current += 1     
                nums[current], nums[lastIndex] = nums[lastIndex], nums[current]
                lastIndex -= 1
            else:
                current += 1
        return nums