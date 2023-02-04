input()
arr = list(map(int, input().split(" ")))

mapping = {0 : "00", 1 : "01", 2 : "10", 3 : "11"}

memo = {}

def do(arr, index, prev):
    state = (index, prev)
    if state in memo:
        return memo[state]

    if index == len(arr):
        return 0
    m = mapping[arr[index]]

    if m[0] == m[1] == "0":
        memo[state] = do(arr, index + 1, "R") + 1
        return memo[state]

    if prev == "G":
        if m[0] == m[1] == "1" or m[1] == "1":
            memo[state] = do(arr, index + 1, "C")
            return memo[state]
        else:
            memo[state] = do(arr, index + 1, "R") + 1
            return memo[state]
    elif prev == "C":
        if m[0] == m[1] == "1" or m[0] == "1":
            memo[state] = do(arr, index + 1, "G")
            return memo[state]
        else:
            memo[state] = do(arr, index + 1, "R") + 1
            return memo[state]
    else:
        if m[0] == m[1] == "1":
            memo[state] = min(do(arr, index + 1, "C"), do(arr, index + 1, "G"))
            return memo[state]
        elif m[0] == "1":
            memo[state] = do(arr, index + 1, "G")
            return memo[state]
        else:
            memo[state] = do(arr, index + 1, "C")
            return memo[state]

print(do(arr, 0, 'R'))