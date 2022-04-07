#LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        arrowCounter = 1
        index = 0
        overlappingRange = points[0]
        
        while index < len(points):
            if self.isOverlap(overlappingRange, points[index]):
                overlappingRange = self.getOverlappingRange(overlappingRange, points[index])
            else:
                arrowCounter += 1
                overlappingRange = points[index]
            index += 1
        
        return arrowCounter
        
    
    def isOverlap(self, range1, range2):
        if range1[1] >= range2[0]:
            return True
        return False
    
    def getOverlappingRange(self, range1, range2):
        if range1[0] <= range2[0] <= range1[1] and range2[1] >= range1[1]:
            return [range2[0], range1[1]]
        if range2[0] <= range1[0] <= range2[1] and range1[1] >= range2[1]:
            return [range1[0], range2[1]]
        if range1[0] <= range2[0] <= range1[1] and range1[0] <= range2[1] <= range1[1]:
            return range2
        if range2[0] <= range1[0] <= range2[1] and range2[0] <= range1[1] <= range2[1]:
            return range1
