class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for account in accounts:
            wealth = max(sum(account), wealth)
        
        return wealth