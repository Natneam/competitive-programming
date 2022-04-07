# LINK TO THE PROBLEM => https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        kS = []
        for i in range(len(arr)-1, 0, -1):
            maxValueIndex = arr.index(max(arr[:i+1]))
            if maxValueIndex == i:
                continue
            self._reverse(arr, 0, maxValueIndex)
            kS.append(maxValueIndex+1)
            self._reverse(arr, 0, i)
            kS.append(i+1)
        
        return kS
    
    def _reverse(self, arr, start, end):
        while end > start:
                arr[end], arr[start] = arr[start], arr[end]
                end -= 1
                start += 1