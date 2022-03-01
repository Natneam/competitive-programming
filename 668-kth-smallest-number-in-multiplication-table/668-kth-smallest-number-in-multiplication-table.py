class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def count(mid):
            count = 0
            for i in range(1, m+1):
                count += min(n, mid//i)
            return count
        
        
        start = 1
        end = m*n
        ans = 0
        
        while start <= end:
            mid = start + (end - start) // 2
            
            if count(mid) < k:
                start = mid + 1
            else:
                ans = mid
                end = mid - 1
        
        return ans