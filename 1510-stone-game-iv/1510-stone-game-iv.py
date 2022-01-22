class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        
        def canWin(num):
            if num in memo:
                return memo[num]
            
            ans = False
            
            i = 1
            while i*i <= num:
                ans = ans or not canWin(num - i*i)
                i += 1
                
            memo[num] = ans
            return ans
        
        return canWin(n)