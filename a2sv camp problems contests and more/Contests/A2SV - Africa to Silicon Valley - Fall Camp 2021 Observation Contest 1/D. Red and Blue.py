def solve(r, b):
    #construct the prefix sum
    r = [0] + r
    b = [0] + b
    for i in range(1, len(r)):
        r[i] = r[i-1] + r[i]
    for i in range(1, len(b)):
        b[i] = b[i-1] + b[i]
    answer = max(r) + max(b)
    return 0 if answer <= 0 else answer


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        input()
        r = list(map(int, input().split()))
        input()
        b = list(map(int, input().split()))
    
        print(solve(r, b), end="\n")

if __name__ == "__main__":
    main()