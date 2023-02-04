n, d = map(int, input().split(" "))
arr = list(reversed(input()))
prev, curr, jump = 0, 0, 0
 
for i in range(len(arr)): 
    if i - prev <= d:
        if arr[i] == "1":
            curr = i
    else:
        prev = curr
        jump += 1
        if i - prev <= d and arr[i] == "1":
            curr = i
 
print(jump + 1) if curr == len(arr) - 1 else print(-1)