_ = input()
arr = list(map(int, input().split(" ")))
arr.sort()

for i in range(int(input())):
    a = int(input())
    l = 0
    r = len(arr) - 1
    ans = l

    while (l <= r):
        mid = l + (r - l) // 2

        if arr[mid] <= a:
            ans = max(ans, mid + 1)
            l = mid + 1
        else:
            r = mid - 1
    
    print(ans)