def solve(arr):
    my_turn = False
    index = 0
    skips = 0
    while index < len(arr) - 2:
        if not my_turn:
            if arr[index] == '0':
                if arr[index+1] == '0':
                    index += 2
                else:
                    index += 1
            else:
                skips += 1
                if arr[index+1] == '0':
                    index += 2
                else:
                    index += 1
        else:
            if arr[index] == '0':
                if arr[index+1] == '0':
                    index += 1
                else:
                    index += 2
            else:
                if arr[index+1] == '0':
                    index += 1
                else:
                    index += 2
        my_turn = not my_turn
    return skips


def main():
    answers = []
    test_cases = int(input())
    for _ in range(test_cases):
        input()
        arr = input().split() + ['0']*3
        answers.append(solve(arr))

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()