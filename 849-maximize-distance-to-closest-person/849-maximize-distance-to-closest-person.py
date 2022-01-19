class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        diff, last = 0, -1
        
        for i  in range(len(seats)):
            if seats[i]:
                diff = max(diff, i if last < 0 else (i - last) // 2)
                last = i
        return max(diff, len(seats) - last - 1)