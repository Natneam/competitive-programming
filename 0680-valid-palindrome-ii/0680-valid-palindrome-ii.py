class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.check(s, 0, len(s) - 1, False, {})
    
    def check(self, s, start, end, flag, memo):
        state = (start, end)
        if state in memo:
            return memo[state]
        
        while start < end:
            if s[start] != s[end]:
                if flag:
                    memo[state] = False
                    return False
                else:
                    memo[state] = self.check(s, start + 1, end, True, memo) or self.check(s, start, end - 1, True, memo)
                    return memo[state]
            start += 1
            end -= 1
        
        memo[state] = True
        return True