# LINK TO THE PROBLEM => https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0
        for city in range(0,len(isConnected)):
            if city not in visited:
                self.dfs(isConnected, visited, city)
                provinces += 1
        return provinces
    
    def dfs(self, isConnected, visited, city1):
        for city2 in range(len(isConnected[city1])):
            if isConnected[city1][city2] == 1 and city2 not in visited:
                visited.add(city2)
                self.dfs(isConnected, visited, city2)