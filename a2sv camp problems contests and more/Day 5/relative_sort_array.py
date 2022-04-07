# LINK TO THE PROBLEM => https://leetcode.com/problems/relative-sort-array/submissions/

class Solution:
    def relativeSortArray(self, arr1, arr2):
        countingArr = [0 for x in range(1001)]
        sortedArr = []
        for i in arr1:
            countingArr[i] += 1
        
        for j in arr2:
            for k in range(countingArr[j]):
                sortedArr.append(j)
            countingArr[j] = 0
        
        for index, value in enumerate(countingArr):
            if value != 0:
                for j in range(value):
                    sortedArr.append(index)
        
        return sortedArr