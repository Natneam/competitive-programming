#LINK TO THE PROBLEM => https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3805/


#Solution one => n^2 space complexity, n^2 time complexity
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        listOfTheMatrix = []
        for row in matrix:
            for item in row:
                listOfTheMatrix.append(item)
                
        listOfTheMatrix.sort()
        
        return listOfTheMatrix[k-1]
