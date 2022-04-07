# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-sideway-jumps/

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        queue = deque()
        visited = set()
        
        queue.append([0,2,0])  # spot on the road ,lane, path length
        visited.add((0,2))
        
        
        while queue:
            currSpot = queue.popleft()
            if currSpot[0] == len(obstacles) - 1:
                return currSpot[2]
            if obstacles[currSpot[0] + 1] == 0 or obstacles[currSpot[0] + 1] != currSpot[1]:
                if (currSpot[0] + 1, currSpot[1]) not in visited:
                    queue.append([currSpot[0]+1, currSpot[1], currSpot[2]])
            else:
                if currSpot[1] == 1:
                    for i in [2,3]:
                        if obstacles[currSpot[0]] != i and (currSpot[0], i) not in visited:
                            visited.add((currSpot[0], i))
                            queue.append([currSpot[0], i, currSpot[2] + 1])
                elif currSpot[1] == 2:
                    for i in [1,3]:
                        if obstacles[currSpot[0]] != i and (currSpot[0], i) not in visited:
                            visited.add((currSpot[0], i))
                            queue.append([currSpot[0], i, currSpot[2] + 1])
                elif currSpot[1] == 3:
                    for i in [1,2]:
                        if obstacles[currSpot[0]] != i and (currSpot[0], i) not in visited:
                            visited.add((currSpot[0], i))
                            queue.append([currSpot[0], i, currSpot[2] + 1])                