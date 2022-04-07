def solve(matrix, col):
    answers = []
    for i in range(col):
        upper_route = matrix[0][-1] - matrix[0][i]
        lower_route = matrix[1][0] - matrix[1][i]
        answers.append(max(lower_route, upper_route))
    
    return min(answers)

def main():
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        col = int(input())
        matrix = [list(map(int, input().split())), list(map(int, input().split()))]
        for i in range(1, col):
            matrix[0][i] = matrix[0][i] + matrix[0][i - 1]
        
        for i in range(col-2, -1, -1):
            matrix[1][i] = matrix[1][i] + matrix[1][i + 1]
        
        answers.append(solve(matrix, col))
    
    for answer in answers:
        print(answer, end="\n")


if __name__ == "__main__":
    main()