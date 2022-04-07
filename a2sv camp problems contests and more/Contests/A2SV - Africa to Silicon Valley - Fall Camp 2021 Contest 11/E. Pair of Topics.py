def bin_search(arr, start, end, num):
    best_so_far = len(arr)
    while start <= end:
        mid = (start + end)//2
        if arr[mid] > num:
            best_so_far = mid
            end = mid - 1
        else:
            start = mid + 1
    return best_so_far

def solve(arr):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        count += len(arr) - bin_search(arr, i+1, len(arr)-1, -arr[i])
    return count

def main():
    topics = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(solve([x[0] - x[1] for x in zip(a,b)]))


if __name__ == "__main__":
    main()