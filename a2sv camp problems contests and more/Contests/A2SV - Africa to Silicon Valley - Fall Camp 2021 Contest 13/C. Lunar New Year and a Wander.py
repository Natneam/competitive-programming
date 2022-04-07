from typing import DefaultDict
import heapq

def solve(n, graph):
    heap = []
    visited = set()
    visited_heap = set()
    answer = []

    heapq.heappush(heap, 1)
    while heap:
        node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)
            answer.append(node)

        for neighbour in graph[node]:
            if neighbour  not in visited_heap:
                heapq.heappush(heap, neighbour)
                visited_heap.add(neighbour)
    return answer
        

def main():
    n, m = list(map(int, input().split()))
    graph = DefaultDict(list)

    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    print(*solve(n, graph), sep=" ", end="\n")

if __name__ == "__main__":
    main()