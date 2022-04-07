import sys
sys.setrecursionlimit(10**8)

def solve(capacity, arr, index, memo):
    if index >= len(arr):
        return 0
    
    if (capacity, index) in memo:
        return memo[(capacity, index)]
    
    if capacity - arr[index][0] < 0:
        val = solve(capacity, arr, index+1, memo)
        memo[(capacity, index)] = val
        return val
    
    new_capacity = capacity - arr[index][0]
    val = max(solve(new_capacity, arr, index+1, memo) + arr[index][1], solve(capacity, arr, index+1, memo))
    memo[(capacity, index)] = val
    return val
    

def main():
    t = int(input())
    for _ in range(t):
        s, n = list(map(int, input().split()))
        arr = []
        for i in range(n):
            # [weight, value]
            arr.append(list(map(int, input().split())))
        print(solve(s, arr, 0, {}))
        
if __name__ == "__main__":
    main()