# LINK TO THE PROBLEM => https://leetcode.com/problems/maximum-average-pass-ratio/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [[ x[0]/x[1] - ((x[0] + 1)/ (x[1] + 1)) ,x[0], x[1]] for x in classes]
        heapq.heapify(classes)
        
        for i in range(extraStudents):
            top = heapq.heappop(classes)
            x = top[1] + 1
            y = top[2] + 1
            old = x/y
            new = (x + 1)/(y + 1)
            heapq.heappush(classes, [old-new, x, y])
        
        return sum([x[1]/x[2] for x in classes])/len(classes)
