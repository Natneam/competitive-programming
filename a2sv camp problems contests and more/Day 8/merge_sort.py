# LINK TO THE PROBELM +> https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self._mergeSort(nums)
        
    def _mergeSort(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return nums
        else:
            start = 0
            end = len(nums)-1
            mid = (start + end)//2 
            sortedArr1 = self._mergeSort(nums[:mid+1])
            sortedArr2 = self._mergeSort(nums[mid+1:])
            return self._merge(sortedArr1, sortedArr2)
            
    def _merge(self, arr1, arr2):
        indicatorInArr1 = 0
        indicatorInArr2 = 0
        
        mergedArr = []
        
        while indicatorInArr1 < len(arr1) and indicatorInArr2 < len(arr2):            
            if arr1[indicatorInArr1] <= arr2[indicatorInArr2]:
                mergedArr.append(arr1[indicatorInArr1])
                indicatorInArr1 += 1
            else:
                mergedArr.append(arr2[indicatorInArr2])
                indicatorInArr2 += 1
        # handling un merged part of the two arrays                
        if indicatorInArr1 < len(arr1):
            while indicatorInArr1 < len(arr1):
                mergedArr.append(arr1[indicatorInArr1])
                indicatorInArr1 += 1

        if indicatorInArr2 < len(arr2):
            while indicatorInArr2 < len(arr2):
                mergedArr.append(arr2[indicatorInArr2])
                indicatorInArr2 += 1
        return mergedArr