class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        for i in range(1, len(w)):
            self.prefix.append(self.prefix[-1] + w[i])
        
    def pickIndex(self) -> int:
        seed = randint(1, self.prefix[-1])
        start, end = 0, len(self.prefix) - 1
        
        while start <= end:
            mid = start + (end - start)//2
            
            ans = start
            if seed <= self.prefix[mid]:
                end = mid - 1
            else:
                start = mid + 1
                ans = start
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()