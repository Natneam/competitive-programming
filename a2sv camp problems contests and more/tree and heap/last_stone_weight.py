# LINK TO THE PROBLEM => https://leetcode.com/problems/last-stone-weight/

import heapq as heap
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1*stones[i] 
        heap.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return -1*stones[0]
            v1 = heap.heappop(stones)            
            v2 = heap.heappop(stones)
            v = abs(v1 - v2)
            if v != 0:
                heap.heappush(stones, -v)
        return 0