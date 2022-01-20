class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def eat_all(rate):
            count = 0
            for p in piles:
                count += (p + rate -1) // rate
            return count
            
        start = 1
        end = max(piles)
        ans = 0
        
        while start <= end:
            mid = start + (end - start)//2
            time = eat_all(mid)
            
            if time <= h:
                ans = mid
                end = mid - 1 
            elif time > h:
                start = mid + 1
        return ans