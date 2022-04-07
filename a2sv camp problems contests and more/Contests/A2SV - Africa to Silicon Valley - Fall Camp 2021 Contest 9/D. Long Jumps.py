test_cases = int(input())
answers = []

for _ in range(test_cases):
    length = int(input())
    array = list(map(int, input().split()))
    
    memo = [-1]*length

    for i in range(len(array)-1, -1, -1):
        index = i
        summation = 0
        while index < len(array):
            if memo[index] > -1:
                summation += memo[index]
                break
            summation += array[index]
            index += array[index]
        memo[i] = summation

    answers.append(max(memo))

for answer in answers:
    print(answer, end="\n")