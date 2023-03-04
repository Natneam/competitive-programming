for _ in range(int(input())):
    input()
    string = input()
    start = 0
    end = len(string) - 1
    res = len(string)

    while start < end:
        if string[start] != string[end]:
            res -= 2
            start += 1
            end -= 1
        else:
            break
    print(res, end="\n")

