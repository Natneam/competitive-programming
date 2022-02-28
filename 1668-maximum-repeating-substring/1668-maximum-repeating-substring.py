class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 1
        while True:
            if word*ans in sequence:
                ans += 1
            else:
                return ans - 1
        