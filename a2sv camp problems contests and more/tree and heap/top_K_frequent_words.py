# LINK TO THE PROBLEM => https://leetcode.com/problems/top-k-frequent-words/
import heapq as heap
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordsDict = dict()
        for i in words:
            if i in wordsDict.keys():
                wordsDict[i] += 1
            else:
                wordsDict[i] = 1
        wordsFreq = [[-v,k] for k,v in wordsDict.items()]
        heap.heapify(wordsFreq)
        output = []
        for i in range(k):
            output.append(heap.heappop(wordsFreq)[1])
        return output