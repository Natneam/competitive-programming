def solve(a):
    maximum = max(a)
    s = [[chr((x%27) + ord('a')) for x in range(maximum+1)]]

    for i in range(len(a)):
        z = [s[-1][x] for x in range(a[i])] + [chr((x + 1)%27 + ord(s[-1][a[i]])) for x in range(maximum - a[i] + 1)]
        s.append(z)
        # print(x)
    print(s)
        



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        solve(a)
if __name__ == "__main__":
    main()