class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(num):
            count = 0
            for i in range(1, m + 1):
                count += min(n, num//i)
            return count
        
        start = 1
        end = m*n
        ans = 0
        
        while start < end:
            mid = start + (end - start) // 2
            if check(mid) < k:
                ans = mid
                start = mid + 1
            else:
                end = mid
        
        return ans + 1