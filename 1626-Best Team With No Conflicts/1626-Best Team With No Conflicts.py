class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        team = sorted(list(zip(ages, scores)))
        def solve(index, max_score, memo):
            state = (index, max_score)
            if state in memo: return memo[state]
            if index == len(team): return 0
            
            res = 0
            if team[index][1] >= max_score:
                res = team[index][1] + solve(index + 1, team[index][1], memo)
            memo[state] = max(res, solve(index + 1, max_score, memo))
            
            return memo[state]
        
        res, memo = 0, {}
        for i in range(len(team)):
            res = max(res, solve(i, 0, memo))
        
        return res