def main():
    n = int(input())
    if n <= 2:
        print(-1)
    else:
        print(" ".join([str(x) for x in range(n, 0, -1)]))

main()
