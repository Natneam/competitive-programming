def solve(s):
    start_index = 0
    end_index = 0
    counts = [0, 0, 0]
    answer = float('inf')
    
    counts[s[0] - 1] += 1

    while start_index <= end_index and end_index <= len(s) - 1:
        if counts[0] == 0 or counts[1] == 0 or counts[2] == 0:
            end_index += 1
            if end_index <= len(s) - 1:
                counts[s[end_index] - 1] += 1
        else:
            counts[s[start_index] - 1] -= 1
            start_index += 1
        
        if counts[0] > 0 and counts[1] > 0 and counts[2] > 0:
            answer = min(answer, end_index - start_index)

    return answer + 1

def main():
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        answer = solve(list(map(int, list((input())))))
        if answer == float('inf'):
            answer = 0
        answers.append(answer)
    
    for answer in answers:
        print(answer, end="\n")


if __name__ == "__main__":
    main()