from typing import DefaultDict

reposts = int(input())

graph = DefaultDict(list)

for _ in range(reposts):
    a, _, b = input().split()
    graph[b.lower()].append(a.lower())


def dfs(graph, start):
    answer = 1
    for node in graph[start]:
        answer = max(answer, dfs(graph, node) + 1)
    return answer

print(dfs(graph, "polycarp"))