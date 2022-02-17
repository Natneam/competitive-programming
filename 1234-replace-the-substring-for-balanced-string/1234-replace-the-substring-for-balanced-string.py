class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        
        ans = len(s)
        
        start = 0
        
        for end in range(len(s)):
            counter[s[end]] -= 1
            
            while start < len(s) and all(counter[x] <=  len(s) // 4 for x in "QWER"):
                ans = min(ans, end - start + 1)
                
                counter[s[start]] += 1
                start += 1
            
        return ans