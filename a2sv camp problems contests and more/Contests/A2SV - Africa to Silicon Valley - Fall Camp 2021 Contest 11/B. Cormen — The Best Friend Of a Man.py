def solve(arr, k):
    for i in range(1, len(arr)):
        if arr[i-1] + arr[i] < k:
            arr[i] += (k - (arr[i-1] + arr[i]))
    return arr


def main():
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    original_arr_sum = sum(arr)

    solve(arr, k)

    updated_arr_sum = sum(arr)

    print(updated_arr_sum - original_arr_sum, end="\n")

    print(*arr, sep=" ", end="\n")

if __name__ == "__main__":
    main()