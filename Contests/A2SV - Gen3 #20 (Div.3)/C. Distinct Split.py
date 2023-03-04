for _ in range(int(input())):
    input()
    arr = input()
    pre = set()
    suf = set()

    prefix = []
    suffix = []

    for i in range(len(arr)):
        pre.add(arr[i])
        prefix.append(len(pre))
        suf.add(arr[len(arr) - 1 - i])
        suffix.append(len(suf))
    suffix = list(reversed(suffix))
    res = 0
    for i in range(1, len(arr)):
        res = max(res, prefix[i - 1] + suffix[i])
    print(res)