# LINK TO THE PROBLEM => https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        minHeap = []
        for item in arr:
            if item <= x:
                maxHeap.append(-item)
            else:
                minHeap.append(item)
        heapq.heapify(maxHeap)        
        heapq.heapify(minHeap)
        
        output = []
        
        for i in range(k):
            topOfMax = None
            topOfMin = None
            
            if maxHeap:
                topOfMax = -heapq.heappop(maxHeap)
            if minHeap:
                topOfMin = heapq.heappop(minHeap)
                
            if topOfMax != None and topOfMin != None:
                if (abs(x - topOfMax) <= abs(x - topOfMin)):
                    output.append(topOfMax)
                    heapq.heappush(minHeap, topOfMin)
                else:
                    output.append(topOfMin)
                    heapq.heappush(maxHeap, -topOfMax)
            elif topOfMax != None:
                output.append(topOfMax)
            elif topOfMin != None:
                output.append(topOfMin)
            else:
                break
        return sorted(output)
            