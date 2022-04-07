# LINK TO THE PROBLEM => https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        modify = 0
        flag = True
        if len(nums) <= 1:
            return len(nums)
        
        if len(nums) == 2:
            if nums[0] == nums[1]: return len(nums)-1
            else: return  len(nums)
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                if flag:
                    modify += 1
                    flag = False
            else: 
                if flag == False:
                    nums[modify] = nums[i]
                modify += 1
                
        return modify if flag == False else modify + 1 