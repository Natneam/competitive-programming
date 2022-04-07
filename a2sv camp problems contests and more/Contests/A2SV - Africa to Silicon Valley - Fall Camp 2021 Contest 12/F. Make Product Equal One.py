def solve(arr):
    count_0, count_negative = 0, 0

    for num in arr:
        if num == 0:
            count_0 += 1
        elif num < 0:
            count_negative += 1
    
    cost = 0

    for num in arr:
        if num < 0:
            cost += -(num + 1)
        elif num > 0:
            cost += num - 1
    if count_0 > 0:
        cost += count_0
    else:
        if count_negative % 2 != 0:
            cost += 2
    
    return cost

def main():
    n = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr))
    
if __name__ == "__main__":
    main()