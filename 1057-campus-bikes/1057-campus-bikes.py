class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # see and record all the distances between pair of bike and worker
        # sort the distances
        # assign each unique bike to a worker according to the ordering from the distance array
        
        distances = [] #[[distance, woker index, bike index], ...] 
        
        def calc_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        for i in range(len(workers)):
            for j in range(len(bikes)):
                distances.append((calc_distance(workers[i], bikes[j]), i, j))
        
        distances.sort()
        visited = set()
        
        ans = [-1 for x in workers]
        
        for distance in distances:
            if ans[distance[1]] == -1 and distance[2] not in visited:
                ans[distance[1]] = distance[2]
                visited.add(distance[2])
        
        return ans
        