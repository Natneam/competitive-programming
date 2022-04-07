# LINK TO THE PROBLEM => https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort() # sorting the array with nlogn time complexity
        counter = 0
        h = 0
        if len(citations) == 0:
            return  len(citations)
        elif len(citations) == 1:
            return len(citations) if citations[0] > 1 else citations[0]
        cMax = citations[-1]
        while True:
            try:
                cIndex = citations.index(counter)
                h = len(citations) - cIndex
                if citations[len(citations)-h] >= h:
                    while len(citations)-h != 0:
                        if citations[len(citations)-h-1] <= h:
                            break
                        else:
                            h += 1
                    break
                        
            except:
                pass
                        
            counter += 1
            if counter > cMax:
                return cMax
        return h