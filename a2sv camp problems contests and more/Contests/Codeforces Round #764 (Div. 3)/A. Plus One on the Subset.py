def main():
    for i in range(int(input())):
        input()
        lst = list(map(int, input().split()))
        lst.sort(reverse=True)
        ans = 0
        for i in range(1, len(lst)):
            ans += lst[i-1] - lst[i]
        
        print(ans, end="\n")

if __name__ == "__main__":
    main()