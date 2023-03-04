t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if a < b: # better walking
        print(a*4)
        continue
    elif b*c*2 < a*c: # better taking the elevetor
        print(b*(4 + c))
        continue
    else: # better taking the stairs till the cth floor then elevetor
        print(a*c + b*(4 - c))
