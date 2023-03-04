n, k = map(int, input().split())
arr = list(map(int, input().split()))

prefixxor = [0]

for ele in arr:
    prefixxor.append(prefixxor[-1]^ele)

history = {}

for i in range(len(prefixxor)):
    if prefixxor[i] not in history:
        history[prefixxor[i]] = i

res = 0
for i in range(len(prefixxor)):
    if k ^ prefixxor[i] in history:
        res = max(res, abs(i - history[k ^ prefixxor[i]]))

print(res)