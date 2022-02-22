class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for i in range(len(columnTitle)):
            ans += (ord(columnTitle[len(columnTitle) - i - 1]) - ord('A') + 1) * 26 ** i 
        return ans