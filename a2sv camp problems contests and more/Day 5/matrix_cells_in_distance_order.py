# LINK TO THE PROBLEM => https://leetcode.com/problems/matrix-cells-in-distance-order/submissions/

import math

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        elementWithDistance = []
        output = []
        for x in range(R):
            for y in range(C):
                elementWithDistance.append([x,y,abs(x-r0)+abs(y-c0)])         
        # return [x[:2] for x in sorted(elementWithDistance, key = lambda a : a[2])]
        countingArr = [0 for x in range(198)]
        for i in elementWithDistance:
            countingArr[i[2]] += 1
        
        for index, value in enumerate(countingArr):
            for v in elementWithDistance:
                if v[2] == index:
                    output.append(v[:2])
        return output