test_cases = int(input())
answers = []
for _ in range(test_cases):
    input()
    number = input()
    count_of_non_zeros = 0

    for i in range(len(number)-1):
        if number[i] != '0':
            count_of_non_zeros += 1
    
    answers.append(sum(list(map(int, list(number)))) + count_of_non_zeros)

for answer in answers:
    print(answer, end="\n")