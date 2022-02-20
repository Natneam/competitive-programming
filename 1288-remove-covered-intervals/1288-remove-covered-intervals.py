class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        def ommit(interval1, interval2):
            a, b = interval1
            c, d = interval2
            
            if c <= a and b <= d:
                return [interval2]
            elif a <= c and d <= b:
                return [interval1]
            
            return [interval1, interval2]
            
        intervals.sort()
        new_intervals = [intervals[0]]
        
        for interval in intervals:
            last = new_intervals.pop()
            for i in ommit( last, interval):
                new_intervals.append(i)
            # print(new_intervals)
        
        return len(new_intervals)