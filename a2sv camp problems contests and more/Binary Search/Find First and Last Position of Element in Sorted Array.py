# link to the problem => https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums)-1
        while start <= end and start < len(nums) and end > -1:
            center = (start + end)//2
            if nums[center] == target:
                return self.startEndIndices(center, target, nums)
            elif nums[center] < target:
                start = center + 1
            else:
                end = center - 1
        return [-1,-1]
        
    def startEndIndices(self, index, target, nums):
        start = index
        end = index
        while start > 0:
            if nums[start-1] ==  target:
                start -= 1
            else:
                break
        while end < len(nums)-1:
            if nums[end + 1] == target:
                end += 1
            else:
                break
        return [start,end]
                
                