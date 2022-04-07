def solve(string):
    start_index = 0
    length = 0
    for i in range(len(string)):
        if string[i] == 'R':
            length = max(length, i - start_index)
            start_index = i
    return length


def main():
    test_cases = int(input())
    answers = []
    for _ in range(test_cases):
        string = 'R'+ input() +'R'
        answers.append(solve(string))
    
    for ann in answers:
        print(ann, end="\n")

if __name__ == "__main__":
    main()