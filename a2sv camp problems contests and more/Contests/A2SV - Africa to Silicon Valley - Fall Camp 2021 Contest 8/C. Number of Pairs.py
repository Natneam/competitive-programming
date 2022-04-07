def number_of_invalid_pairs(l, r, numbers):
    numbers.sort()

    invalid_pairs = 0
    # #excluding pairs which have smaller sum
    # for i in range(len(numbers)):
    #     index = len(numbers) - i - 1
    #     if numbers[index] + numbers[0] < l:
    #         invalid_pairs += index
    
    # #excluding pairs which have larger sum
    # for index in range(len(numbers)):
    #     if numbers[index] + numbers[len(numbers)-1] > r:
    #         invalid_pairs += len(numbers) - 1 - index
    
    return invalid_pairs
def comb_2(n):
    return (n*(n-1))//2

if __name__ == "__main__":
    test_cases = int(input())
    answers = []
    for i in range(test_cases):
        n, l, r = list(map(int, input().split()))
        numbers = list(map(int, input().split()))
        
        answers.append(comb_2(n) - number_of_invalid_pairs(l, r, numbers))
    
    for i in range(len(answers)):
        print(answers[i], end="\n")
