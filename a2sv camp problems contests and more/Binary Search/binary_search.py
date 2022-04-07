# LINK TO THE PROBLEM => https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._binarySearch(nums, 0, len(nums)-1, target)
        
    def _binarySearch(self,nums, start, end, target):
        if start > end:
            return -1
        middle = (start + end )// 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            start = middle + 1
            return self._binarySearch(nums, start,end, target)
        else:
            end = middle - 1
            return self._binarySearch(nums, start,end, target)