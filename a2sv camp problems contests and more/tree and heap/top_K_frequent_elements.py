# LINK TO THE PROBLEM => https://leetcode.com/problems/top-k-frequent-elements/
import heapq as heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsDict = dict()
        for i in nums:
            if i in numsDict.keys():
                numsDict[i] += 1
            else:
                numsDict[i] = 1
        numsFreq = [[-v,k] for k,v in numsDict.items()]
        heap.heapify(numsFreq)
        output = []
        for i in range(k):
            output.append(heap.heappop(numsFreq)[1])
        return output
            