class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        for x in range(1, n//2 + 1):
            res.append(x)
            res.append(-x)
        
        if len(res) != n:
            res.append(0)
        
        return res