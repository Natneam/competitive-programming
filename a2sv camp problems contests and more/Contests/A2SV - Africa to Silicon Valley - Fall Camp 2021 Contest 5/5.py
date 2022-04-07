# LINK TO THE PROBLEM => https://codeforces.com/problemset/problem/1593/E

from collections import defaultdict, deque

testcases = int(input())
remaining_nodes = list()

for i in range(testcases):
    input()
    graph = defaultdict(list)

    n, k = map(int, input().split())

    for i in range(n-1):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    indegree = [0]* (n+1)
    queue = deque()
    temp = list()

    #setting up the indegree
    for start_node in graph:
        for destination_node in graph[start_node]:
            indegree[destination_node] += 1

    #adding all the nodes with indegree 1
    for i in range(len(indegree)):
        if indegree[i] <= 1:
            queue.append(i)
    
    count_of_deleted_nodes = 0

    while queue and k > 0:
        node = queue.popleft()
        count_of_deleted_nodes += 1

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 1:
                temp.append(neighbor)
                
        if len(queue) == 0:
            k -= 1
            queue = deque(temp)
            temp = []

    remaining_nodes.append(n + 1 - count_of_deleted_nodes)

for i in remaining_nodes:
    print(i)