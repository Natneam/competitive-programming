# LINK TO THE PROBLEM => https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answersDict = dict()
        
        for answer in answers:
            if answer in answersDict.keys():
                answersDict[answer] += 1
            else:
                answersDict[answer] = 1
        
        output = 0
        for key in answersDict.keys():
            output += (answersDict[key] // ( key + 1))*(key+1) + ((key +1 ) if answersDict[key] % (key + 1) else 0 )
        
        return output
