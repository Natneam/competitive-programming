LINK TO THE PROBLEM => https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answerDict = dict()
        for i in strs:
            iSorted = "".join(sorted(i)) 
            if iSorted not in answerDict:
                answerDict[iSorted] = [i]
            else:
                answerDict[iSorted].append(i)
        
        return [x for x in answerDict.values()]