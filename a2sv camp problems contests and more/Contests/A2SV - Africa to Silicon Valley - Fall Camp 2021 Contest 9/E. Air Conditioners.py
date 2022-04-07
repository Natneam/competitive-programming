def solve(arr):
    minimum = arr[0]
    for i in range(len(arr)):
        arr[i] = min(minimum, arr[i])
        minimum = arr[i] + 1
    
    minimum = arr[-1]
    for i in range(len(arr)-1, -1, -1):
        arr[i] = min(minimum, arr[i])
        minimum = arr[i] + 1


if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        input()
        n, k = list(map(int, input().split()))
        arr= [float('inf')]*n

        ac_index = list(map(int, input().split()))
        ac_value = list(map(int, input().split()))

        for i in range(len(ac_index)):
            arr[ac_index[i]-1] = ac_value[i]
        
        solve(arr)
        arr = list(map(str, arr))
        print(" ".join(arr))