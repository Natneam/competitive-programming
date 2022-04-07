# LINK TO THE PROBLEM => https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        frequencyDict = dict()
        for i in order:
            frequencyDict[i] = 0
        
        for i in str:
            if i in frequencyDict.keys():
                frequencyDict[i] += 1
        
        result = ''
        for i in order:
            result = result + i*frequencyDict[i]
        
        for i in str:
            if i not in frequencyDict:
                result += i

        return result
