def union(parents, a, b):
    a_p = find(parents, a)
    b_p = find(parents, b)

    if a_p != b_p:
        parents[b_p - 1] = a_p
        return True
    return False

def find(parents, a):
    node = a
    while parents[node - 1] != node:
        node = parents[node - 1]
    
    return node


def solve(arr, n):
    arr.sort()

    visited = set()
    parents = [i+1 for i in range(n)]
    cost = 0

    for edge in arr:
        if edge[2] in visited:
            continue

        if union(parents, edge[1], edge[2]):
            visited.add(edge[2])
            cost += edge[0]
    
    return cost if len(visited) == n - 1 else -1

    



def main():
    n = int(input())
    input()
    apps = int(input())
    lst = []
    for _ in range(apps):
        app = list(map(int, input().split()))
        lst.append([app[2], app[0], app[1]])
    print(solve(lst, n))

if __name__ == "__main__":
    main()