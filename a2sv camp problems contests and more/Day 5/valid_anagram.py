# LINK TO THE PROBLEM => https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [ord(x) for x in list(s)]
        t = [ord(x) for x in list(t)]
        
        # using counting sort
        countingArrS = [0 for x in range(122 - 97 + 1)]
        countingArrT = [0 for x in range(122 - 97 + 1)]
        sSorted = []
        tSorted = []
        for value in s:
            countingArrS[value-97] += 1
        for value in t:
            countingArrT[value-97] += 1
        
        for index, value in enumerate(countingArrS):
            for j in range(value):
                sSorted.append(index+97)
        for index, value in enumerate(countingArrT):
            for j in range(value):
                tSorted.append(index+97)
        if sSorted == tSorted:
            return True
        return False