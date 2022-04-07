test_cases = int(input())
answers = []

for i in range(test_cases):
    a, b, c, m = list(map(int, input().split()))
    lst = sorted([a, b, c])

    max_m = sum(lst) - 3
    min_m = lst[2] - lst[1] - lst[0] - 1

    if max_m >= m >= min_m:
        answers.append("YES")
    else:
        answers.append("NO")


for answer in answers:
    print(answer)