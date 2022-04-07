# LINK TO THE PROBLEM => https://codeforces.com/problemset/problem/47/B

from collections import defaultdict, deque
graph = defaultdict(list)

for i in range(3):
    coin_weighting = input()
    if coin_weighting[1] == '<':
        graph[coin_weighting[0]].append(coin_weighting[2])
    else:
        graph[coin_weighting[2]].append(coin_weighting[0])

indegree = [0, 0, 0]

for i in graph:
    for j in graph[i]:
        indegree[ord(j) - ord('A')] += 1

#bfs
queue = deque()
answer = []

## put all the nodes with indegree == 0 in the queue
for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(chr(ord('A') + i))
        answer.append(chr(ord('A') + i))
if len(answer) == 0:
    print("Impossible")

while queue:
    coin = queue.pop()
    for neighbor in graph[coin]:
        indegree[ord(neighbor) - ord('A')] -= 1
        if indegree[ord(neighbor) - ord('A')] == 0:
            queue.append(neighbor)
            answer.append(neighbor)

print("".join(answer))
