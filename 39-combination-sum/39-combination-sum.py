class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(candidates, 0, target, {})
    
    def helper(self, candidates, start, target, memo):
        if (target, start) in memo:
            return memo[(target, start)]
        
        if target == 0:
            return [[]]
        
        if target < 0:
            return []
        
        if start == len(candidates):
            return []
        
        values = []
        for i in range(start,len(candidates)):
            for item in self.helper(candidates, i, target - candidates[i], memo):
                values.append([candidates[i]] + item)
        
        memo[(target, start)] = values
        return values