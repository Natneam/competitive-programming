import sys
sys.setrecursionlimit(10**5)

def solve(joy_sticks, memo):
    joy_sticks = tuple(sorted(joy_sticks))

    if joy_sticks in memo:
        return memo[joy_sticks]
    
    if joy_sticks[0] < 0:
        memo[joy_sticks] = -1
        return -1
    
    if joy_sticks[0] == 0:
        memo[joy_sticks] = 0
        return 0
    
    val = max(solve([joy_sticks[0] + 1, joy_sticks[1] - 2], memo), solve([joy_sticks[0] - 2, joy_sticks[1] + 1], memo)) + 1
    memo[joy_sticks] = val

    return val

def main():
    joy_sticks = list(map(int, input().split()))
    print(solve(joy_sticks, {}))

if __name__ == "__main__":
    main()