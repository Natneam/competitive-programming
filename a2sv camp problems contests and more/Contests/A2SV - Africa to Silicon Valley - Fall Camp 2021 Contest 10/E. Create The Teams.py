def solve(lst, k):
    start_index = len(lst) - 1
    end_index = len(lst) - 1
    lst.sort()
    answer = 0

    while start_index >= 0:
        if lst[start_index] * (end_index - start_index + 1) >= k:
            answer += 1
            start_index -= 1
            end_index = start_index
        else:
            start_index -= 1
    
    return answer



def main():
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        n, k = list(map(int, input().split()))
        lst = list(map(int, input().split()))
        answer = solve(lst, k)
        answers.append(answer)
    
    for answer in answers:
        print(answer, end="\n")


if __name__ == "__main__":
    main()