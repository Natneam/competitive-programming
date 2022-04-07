n, t = list(map(int, input().split()))

lst = list(map(int, input().split()))

index = 1
while index <= len(lst):
    if index == t:
        break
    index = (index + lst[index - 1])

if index == t:
    print("YES")
else:
    print("NO")