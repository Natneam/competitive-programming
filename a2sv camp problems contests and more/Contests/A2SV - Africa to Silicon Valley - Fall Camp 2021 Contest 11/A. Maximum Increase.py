def solve(arr):
    length = 1
    start_index = 0
    prev = start_index

    for i in range(1, len(arr)):
        if arr[i] > arr[prev]:
            length = max(length, i - start_index + 1)
            prev = i
        else:
            start_index = i
            prev = start_index
    
    return length

def main():
    input()
    arr = list(map(int, input().split()))
    print(solve(arr))

if __name__ == "__main__":
    main()