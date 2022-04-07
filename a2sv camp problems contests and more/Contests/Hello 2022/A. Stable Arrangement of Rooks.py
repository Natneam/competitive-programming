def main():
    t = int(input())
    ans = []
    for _ in range(t):
        n, k = list(map(int, input().split()))
        if n // 2 + 1 < k:
            ans.append("-1")
        else:
            arr = []
            for i in range(n):
                if i % 2 == 0 and k > 0:
                    arr .append("."*i + 'R' + '.'*(n - i - 1))
                    k -= 1
                else:
                    arr.append("."*n)
            ans.append("\n".join(arr))
    print("\n".join(ans))
if __name__ == "__main__":
    main()