# LINK TO THE PROBLEM => https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            mapping, valuesSet, isFinished = {}, set(), True
            
            for index in range(len(word)):
                if pattern[index] not in mapping:
                    if word[index] not in valuesSet:
                        mapping[pattern[index]] = word[index]
                        valuesSet .add(word[index])
                    else:
                        isFinished = False
                        break
                else:
                    if mapping[pattern[index]] != word[index]:
                        isFinished = False
                        break
                    
            if isFinished: output.append(word)
        return output
            