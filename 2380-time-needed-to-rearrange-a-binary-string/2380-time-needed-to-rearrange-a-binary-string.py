class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        count = 0
        for i in range(len(s)):
            j = 1
            swapped = False
            while j < len(s):
                if s[j - 1] < s[j]:
                    swapped = True
                    s[j - 1], s[j] = s[j], s[j - 1]
                    j += 1
                j += 1
            count += 1 if swapped else 0
        return count