# LINK TO THE PROBLEM => https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        maxHeap = [-x for x in nums]
        heapq.heapify(maxHeap)
        for i in range(k):
            try:
                heapq.heappush(self.minHeap, -heapq.heappop(maxHeap))
            except:
                break

    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap, val)
            topOfHeap = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, topOfHeap)
            return topOfHeap
    
        topOfHeap = heapq.heappop(self.minHeap)
        if val > topOfHeap:
            heapq.heappush(self.minHeap, val)
            topOfHeap = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, topOfHeap)
            return topOfHeap
        heapq.heappush(self.minHeap, topOfHeap)
        return topOfHeap
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)