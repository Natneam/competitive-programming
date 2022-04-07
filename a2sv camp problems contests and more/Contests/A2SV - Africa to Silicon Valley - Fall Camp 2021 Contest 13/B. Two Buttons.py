# def solve(n, m):
#     if n >= m:
#         return n - m

#     ops = 0
#     if m % 2 != 0: 
#         ops += 1
#         m = m + 1
    
#     while n != (m // 2):
#         if n * 2 <= (m // 2) + 1:
#             n = n * 2
#         else:
#             n -= 1
#         ops += 1
#     return ops + 1

import sys
sys.setrecursionlimit(10**6)

def solve(n, m):
    if n >= m:
        return n - m
    
    ops = 1
    if m % 2 != 0: 
        ops += 1
        m = m + 1
    
    return ops + solve(n, m//2)
    

def main():
    n, m = list(map(int, input().split()))
    print(solve(n, m))

if __name__ == "__main__":
    main()
