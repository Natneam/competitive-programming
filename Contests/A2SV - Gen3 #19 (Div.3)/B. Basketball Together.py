N, D = list(map(int, input().split(" ")))
arr = sorted(list(map(int, input().split(" "))))

start = 0
end = len(arr) - 1
res = 0

while end > start:
    if arr[end] > D:
        end -= 1
        continue

    x = D // arr[end]
    start += x
    end -= 1
    res += 1

print(res)