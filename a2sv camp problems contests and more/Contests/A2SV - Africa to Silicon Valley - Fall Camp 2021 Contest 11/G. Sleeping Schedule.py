import sys
sys.setrecursionlimit(10**6)

def solve(arr, index, start, end, hours, prev_val, memo):
    if index == len(arr):
        return 0
    
    state = (index, prev_val)

    if state in memo:
        return memo[state]
    
    val1 = 0
    val2 = 0
    
    sleeping_hour = prev_val + arr[index]
    if start <= sleeping_hour % hours <= end:
        val1 += 1
    
    if start <= (sleeping_hour - 1) % hours <= end:
        val2 += 1
    
    value = max(solve(arr, index + 1, start, end, hours, sleeping_hour % hours, memo) + val1, solve(arr, index + 1, start, end, hours, (sleeping_hour - 1) % hours , memo) + val2)
    memo[state] = value
    return value

def main():
    n, h, l, r = list(map(int, input().split()))
    a = list(map(int, input().split()))
    memo = {}
    print(max(solve(a, 1, l, r, h, a[0], memo), solve(a, 1, l, r, h, a[0] - 1, memo)), end="\n")

if __name__ == "__main__":
    main()