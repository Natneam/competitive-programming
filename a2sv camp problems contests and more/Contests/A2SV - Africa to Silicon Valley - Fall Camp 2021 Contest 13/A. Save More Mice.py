def solve(n, k, mices):
    mices.sort()
    cats_pos = 0
    while mices and mices[-1] > cats_pos:
        x = mices.pop()
        cats_pos += (n - x)
    
    return k - len(mices)


def main():
    t = int(input())
    answers = []
    for _ in range(t):
        n, k = list(map(int, input().split()))
        mices = list(map(int, input().split()))

        answers.append(solve(n, k,  mices))
    print(*answers, sep="\n")

if __name__ == "__main__":
    main()