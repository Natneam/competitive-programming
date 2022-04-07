def solve(labels, prices):
    arr = []
    for i in labels:
        arr.append(prices[i-1])
    
    for i in range(len(labels)):
        index = len(labels) - 1 - i
        if i < len(prices) and arr[index] > prices[i]:
            arr[index] = prices[i]
        else:
            break
    return sum(arr)

def main():
    t = int(input())
    for _ in range(t):
        n, m = list(map(int, input().split()))
        labels = list(map(int, input().split()))
        prices = list(map(int, input().split()))
        print(solve(sorted(labels), prices), end="\n")
if __name__ == "__main__":
    main()