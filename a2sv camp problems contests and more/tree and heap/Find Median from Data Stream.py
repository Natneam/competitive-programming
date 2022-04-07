# LINK TO THE PROBLEM => https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        """
        initialize your data structures here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == 0 and len(self.maxHeap) == 0:
            heapq.heappush(self.minHeap, num)
        elif len(self.minHeap) == 1 and len(self.maxHeap) == 0:
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            # compare the tops and add it into one of the heaps           
            topOfMaxHeap = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.maxHeap, -topOfMaxHeap)
            
            if topOfMaxHeap >= num:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
            
            #adjusting the size of the heaps
            if len(self.minHeap) < len(self.maxHeap):
                topOfMaxHeap = -heapq.heappop(self.maxHeap)
                heapq.heappush(self.minHeap, topOfMaxHeap)
            if len(self.minHeap) > len(self.maxHeap) + 1:
                topOfMinHeap = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -topOfMinHeap)   

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            topOfMaxHeap = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.maxHeap, -topOfMaxHeap)
            topOfMinHeap = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, topOfMinHeap)
            return (topOfMinHeap + topOfMaxHeap)/2
        else:
            topOfMinHeap = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, topOfMinHeap)
            return topOfMinHeap


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()