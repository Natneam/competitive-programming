n, k = list(map(int, input().split()))

def combination(n, k):
    combinations = list()
    for i in range(1, n+1):
        copy_of_k = k
        for j in range(k):
            if copy_of_k > 0:
                temp = j + i + 1 % n
                temp = temp % n if temp > n else temp
                combinations.append((i, temp))
                copy_of_k -= 1
            else:
                break
    return combinations
def comb_2(n):
    return int((n * (n-1))/2)

if comb_2(n) // n < k:
    print(-1)
else:
    print(n*k)
    for item in sorted(combination(n, k)[:n*k]):
        print(f"{item[0]} {item[1]}")