class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        
        for i in s:
            freq[i] += 1
            
        for j in t:
            freq[j] -= 1
        
        for i in freq:
            if freq[i] < 0:
                return i
        
        