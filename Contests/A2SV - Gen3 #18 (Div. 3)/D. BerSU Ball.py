input()
boys = sorted(map(int, input().split(" ")))
input()
girls = sorted(map(int, input().split()))

i = j = 0
ans = 0

while (i < len(boys) and j < len(girls)):
    if abs(boys[i] - girls[j]) > 1:
        if boys[i] < girls[j]:
            i += 1
        else:
            j += 1
    else:
        i += 1
        j += 1
        ans += 1
print(ans)