class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        res = num
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                temp = s[::]
                temp[i], temp[j] = temp[j], temp[i]
                res = max(res, int("".join(temp)))
        return res