# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-88/problems/maximize-distance-to-closest-person/

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = None
        start = second = 0
        maxDiff = 0
        while second < len(seats):
            if seats[second] == 1:
                if first == None:
                    first = second
                    maxDiff = first*2
                else:
                    if (second-first) >= maxDiff:
                        maxDiff = (second-first)
                    first = second
            second += 1
        if seats[second-1] == 0:
            # print (f" (len(seats)-1-first)*2):{ (len(seats)-1-first)*2}")
            maxDiff = max(maxDiff, (len(seats)-1-first)*2)            
        return maxDiff // 2