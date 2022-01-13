class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        arr = []
        mapping = {}
        for i, p in enumerate(points):
            start = (p[0], -1, i)
            end = (p[1], 1, i)
            mapping[start] = end
            arr.append(start)
            arr.append(end)
        
        arr.sort()
        count = 0
        
        starts = set()
        visited_ends = set()
        
        for i in arr:
            if i[1] == -1:
                starts.add(i)
            elif i not in visited_ends:
                count += 1
                for s in starts:
                    visited_ends.add(mapping[s])
                starts = set()
        return count