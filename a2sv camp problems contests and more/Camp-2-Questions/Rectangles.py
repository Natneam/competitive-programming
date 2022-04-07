n, m = map(int, input().split())

answer = 0
matrix = []

for i in range(n):
   matrix.append(list(map(int, input().split())))

for i in range(n):
   answer += (2**(matrix[i].count(1)) + 2**(matrix[i].count(0)) - 2)

for i in range(m):
    count_of_0, count_of_1 = 0, 0
    for j in range(n):
        if matrix[j][i] == 0:
            count_of_0 += 1
        else:
            count_of_1 += 1
    
    answer += (2**(count_of_1) - count_of_1 - 1 + 2**(count_of_0) - count_of_0 - 1)

print(answer)

