# Link TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-112/problems/bag-of-tokens/

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        startPointer  = 0       
        endPointer = len(tokens) - 1
        score = 0
        maximum = 0 
        while startPointer <= endPointer:
            if tokens[startPointer] <= P:
                score += 1
                if score > maximum:
                    maximum = score
                P -= tokens[startPointer]
                startPointer += 1
            else:
                if score >= 1:
                    score -= 1
                    P += tokens[endPointer]
                    endPointer -= 1
                else:
                    return maximum
        return maximum
        