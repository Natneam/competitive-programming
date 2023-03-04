for _ in range(int(input())):
    input()
    arr = list(map(int, input().split(" ")))
    arr = sorted([[arr[i], i] for i in range(len(arr))])
    res = []
    i = 0

    while i < len(arr):
        if arr[i - 1][0] == 0:
            i += 1
        
        for j in range(i+1, len(arr)):
            if arr[i][0] == 0:
                i += 1
                break
            if arr[j][0] == 0:
                break
            
            res.append([arr[i][1] + 1, arr[j][1] + 1])
            arr[i][0] -= 1
            arr[j][0] -= 1
    
    print(res)

        
