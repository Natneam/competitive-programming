for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    if sum(lst) % n == 0:
        print(0, end="\n")
    else:
        print(1, end="\n")