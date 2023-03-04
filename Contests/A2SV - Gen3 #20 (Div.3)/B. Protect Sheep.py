R, C = list(map(int, input().split()))
_map = []
for i in range(R):
    _map.append(list(input()))

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

res = "YES"
for i in range(R):
    for j in range(C):
        if _map[i][j] == "S":
            for d in dirs:
                if 0 <= i + d[0] < R and 0 <= j + d[1] < C:
                    if _map[i + d[0]][j + d[1]] == "W":
                        res = "NO"
                    elif _map[i + d[0]][j + d[1]] == ".":
                        _map[i + d[0]][j + d[1]] = "D"
print(res)
if res == "YES":
    for r in _map:
        print("".join(r))


