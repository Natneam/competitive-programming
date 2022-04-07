import heapq

def solve(num):
    even_heap = []
    odd_heap = []
    answers = []

    for i in range(1,num+1):
        if i % 2 == 0:
            heapq.heappush(even_heap, -i)
        else:
            heapq.heappush(odd_heap, -i)
    
    while True:

        if len(even_heap) == 1 and len(odd_heap) == 1:
            answers.append([heapq.heappop(even_heap), heapq.heappop(odd_heap)])
            return (-sum(answers[-1]) // 2) + 1, answers
        
        if len(even_heap) == 2 and len(odd_heap) == 0:
            answers.append([heapq.heappop(even_heap), heapq.heappop(even_heap)])
            return -sum(answers[-1]) // 2 , answers
        
        if len(odd_heap) == 2 and len(even_heap) == 0:
            answers.append([heapq.heappop(odd_heap), heapq.heappop(odd_heap)])
            return -sum(answers[-1]) // 2 , answers
        
        if len(even_heap) != 0:
            even =  heapq.heappop(even_heap)
        else:
            even = float('inf')
        
        if len(odd_heap) != 0:
            odd =  heapq.heappop(odd_heap)
        else:
            odd = float('inf')
        
        if even < odd:
            if odd != float('inf'):
                heapq.heappush(odd_heap, odd)
            answers.append([even, heapq.heappop(even_heap)])
            result = sum(answers[-1]) // 2
        else:
            if even != float('inf'):
                heapq.heappush(even_heap, even)
            answers.append([odd, heapq.heappop(odd_heap)])
            result = sum(answers[-1]) // 2

        if result % 2 == 0:
            heapq.heappush(even_heap, result)
        else:
            heapq.heappush(odd_heap, result)

def main():
    test_cases = int(input())
    numbers = [int(input()) for _ in range(test_cases)]
    for num in numbers:
        answer = solve(num)
        print(answer[0], end="\n")

        for i in answer[1]:
            print(f"{-i[0]} {-i[1]}", end="\n")

if __name__ == "__main__":
    main()