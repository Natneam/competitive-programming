import heapq

def solve(lst):
    lst = [(-lst[i], i) for i in range(len(lst))]
    heapq.heapify(lst)
    start = 0
    end =len(lst) - 1

    pivot = None

    while start <= end:
        curr_max = heapq.heappop(lst)
        if curr_max[1] == start:
            start += 1
            continue
        elif curr_max[1] == end:
            end -= 1
            continue
        pivot = curr_max[1]
        break

    if pivot:
        return [True, [str(pivot), str(pivot + 1), str(pivot + 2)]]
    else:
        return [False, []]
        


def main():
    test_cases = int(input())
    answers = []
    for _ in range(test_cases):
        input()
        lst = list(map(int, input().split()))

        answers.append(solve(lst))
    
    for answer in answers:
        if answer[0]:
            print("YES", end="\n")
            print(" ".join(answer[1]), end="\n")
        else:
            print("NO", end="\n")

if __name__ == "__main__":
    main()