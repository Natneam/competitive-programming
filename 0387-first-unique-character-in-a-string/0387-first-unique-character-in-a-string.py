class Solution:
    def firstUniqChar(self, s: str) -> int:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        for i in range(len(s)):
            if s[i] in last:
                if last[s[i]] == i:
                    return i
                else:
                    del last[s[i]]
            
        return -1