from math import comb

n, m, t = map(int, input().split())

possiblities = 0

for i in range(4, t):
    possiblities += comb(n, i) * comb(m,  t-i)

print(possiblities)