# LINK TO THE PROBLEM => https://leetcode.com/problems/k-closest-points-to-origin/
import math
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        pointsWithDistance = [x+[math.sqrt((x[0]**2) + (x[1]**2))] for x in points]
        # sorting the array with nlog(n) time complexity
        pointsWithDistance.sort(key=lambda lst:lst[2])
        
        return [x[:2] for x in pointsWithDistance[:K]]