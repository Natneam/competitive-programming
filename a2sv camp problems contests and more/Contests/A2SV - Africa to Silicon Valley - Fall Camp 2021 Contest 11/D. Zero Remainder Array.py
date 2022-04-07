from typing import DefaultDict


def solve(arr, k):
    arr = [k - (x%k) for x in arr if (x%k)]
    freq = DefaultDict(int)

    #if we don't have any reminder
    if len(arr) == 0:
        return 0
    
    for i in arr:
        freq[i] += 1
    
    # find the maximum frequency
    maximum = [arr[0], 0]
    for i in freq:
        if freq[i] > maximum[1]:
            maximum = [i, freq[i]]
        elif freq[i] == maximum[1] and i > maximum[0]:
            maximum[0] = i    
    return (maximum[1] - 1) * k + maximum[0] + 1



def main():
    test_cases = int(input())
    answers = []
    for _ in range(test_cases):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        answers.append(solve(arr, k))
    
    for an in answers:
        print(an, end="\n")

if __name__ == "__main__":
    main()