class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        i = 0
        while i <= n:
            c_i = i
            while c_i:
                ans[i] += c_i & 1
                c_i >>= 1
            i += 1
        return ans