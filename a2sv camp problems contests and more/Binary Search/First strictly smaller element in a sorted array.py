def smallest(arr, target):
    start = 0
    end = len(arr) - 1
    best_so_far = -1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] < target:
            best_so_far = mid
            start = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
    return best_so_far

if __name__ == "__main__":
    print(smallest([1, 2, 3, 5, 8, 12], 6))