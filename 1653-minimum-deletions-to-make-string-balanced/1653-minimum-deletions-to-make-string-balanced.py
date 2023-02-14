class Solution:
    def minimumDeletions(self, s: str) -> int:
        prefix = [0]
        suffix = [0]
        
        for i in range(len(s)):
            prefix.append(prefix[-1])
            if s[i] == 'b':
                prefix[-1] += 1
        
        for i in range(len(s) - 1, -1, -1):
            suffix.append(suffix[-1])
            if s[i] == 'a':
                suffix[-1] += 1
                
        suffix = list(reversed(suffix))
        
        res = float('inf')
        for i in range(len(prefix) - 1):
            res = min(res, prefix[i] + suffix[i + 1])
        
        return res if res != float('inf') else 0