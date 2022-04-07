from collections import deque, namedtuple
from typing import DefaultDict

def solve(n, graph):
    answers = [1]*(n+1)

    indegree = [0]*(n+1)

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1
    queue = deque()
    for i in range(len(indegree)):
        if i == 0:
            continue
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        node = queue.popleft()
        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                if node > neighbour:
                    answers[neighbour] = max(answers[neighbour], answers[node]+1)
                queue.append(neighbour)
    if max(indegree[1:]) != 0:
        return -1
    return max(answers)


def main():
    test_cases = int(input())
    answers = []
    for _ in range(test_cases):
        n = int(input())
        graph = DefaultDict(list)
        for i in range(1, n+1):
            lst = list(map(int, input().split()))
            if len(lst) == 1:
                continue
            for j in range(1, len(lst)):
                graph[lst[j]].append(i)

        answers.append(solve(n, graph))

    for answer in answers:
        print(answer, end="\n")

if __name__ == "__main__":
    main()