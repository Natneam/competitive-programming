test_cases = int(input())

answers = []

for _ in range(test_cases):
    n, k = list(map(int, input().split()))
    n = n - 1
    count = 0
    while n > 0 and 2**(count) < k:
        n -= 2**(count)
        count += 1
    if n <= 0:
        answers.append(count)
    else:
        if n % k == 0:
            answers.append(count + (n//k))
        else:
            answers.append(count + (n//k) + 1)

for answer in answers:
    print(answer, end="\n")