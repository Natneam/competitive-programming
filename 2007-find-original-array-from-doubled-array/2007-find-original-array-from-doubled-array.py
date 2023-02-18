class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = Counter(changed)
        changed.sort()
        res = []
        if counter[0] % 2: return []
        
        for c in changed:
            if c not in counter:
                continue
            
            if c*2 in counter:
                res.append(c)
                counter[c] -= 1
                counter[c*2] -= 1
                
                if counter[c] == 0:
                    del counter[c]
                if counter[c*2] == 0:
                    del counter[c*2]
            else:
                return []

        
        return res