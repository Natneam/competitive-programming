class Solution:
    def racecar(self, target: int) -> int:
        heap = [(0,0,1),(0,0,-1)]
        visited = defaultdict(lambda: float('inf'))
        while heap:
            step, pos, speed = heapq.heappop(heap)
            if pos < 0:
                continue
            if step >= visited[(pos, speed)]:
                continue
            visited[(pos,speed)] = step
            if pos == target:
                return step
            heapq.heappush(heap,(step+1,pos+speed,speed*2))
            if speed <= 0:
                heapq.heappush(heap,(step+1, pos,1))
            else:
                heapq.heappush(heap,(step+1, pos,-1))
