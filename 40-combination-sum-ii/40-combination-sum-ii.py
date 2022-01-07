class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.helper(sorted(candidates), 0, target, {})
        
    def helper(self, candidates, index, target, memo):
        if (target, index) in memo:
            return memo[(target, index)]
        if target == 0:
            return [[]]
        
        if target < 0 or index == len(candidates):
            return []
        
        values = set()
        
        for i in range(index, len(candidates)):
            for item in self.helper(candidates, i + 1, target - candidates[i], memo):
                values.add(tuple([candidates[i]] + list(item)))
        memo[(target, index)] = values
        return values