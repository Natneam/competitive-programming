from typing import DefaultDict
import sys

sys.setrecursionlimit(10**5)

def dfs(start, graph, visited):
    if start in visited:
        return 0
    maximum = 0
    for i in graph[start]:
        maximum = max(maximum, dfs(i, graph, visited) + 1)
        visited.add(i)
    
    return maximum

def solve(n, graph, parent_nodes):
    visited = set()
    maximum = 0
    for i in parent_nodes:
        if i not in visited:
            maximum = max(maximum, dfs(i, graph, visited) + 1)
            visited.add(i)
    return maximum



def main():
    n = int(input())
    graph = DefaultDict(list)
    parent_nodes = []
    for i in range(1, n+1):
        val = int(input())
        if  val == -1:
            parent_nodes.append(i)
        else:
            graph[val].append(i)
    print(solve(n, graph, parent_nodes))

if __name__ == "__main__":
    main()