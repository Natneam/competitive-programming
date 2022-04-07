from collections import deque

test_cases = int(input())

colors = {'R' : 'B', 'B' : 'R'}

answers = []

def is_valid(row, index):
    if 0 <= index < len(row) and row[index] == '?':
        return True
    return False 

for _ in range(test_cases):
    lenght = int(input())
    row = list(input())
    
    #knowing the prefield fields
    queue = deque()
    visited = set()
    for i in range(len(row)):
        if row[i] =='B' or row[i] == 'R':
            queue.append(i)
            visited.add(i)
    
    if len(queue) == 0:
        row[0] = 'B'
        queue.append(0)
        visited.add(0)
    
    while queue:
        curr_square = queue.popleft()
        
        if is_valid(row, curr_square + 1):
            row[curr_square + 1] = colors[row[curr_square]]
            queue.append(curr_square + 1)
        
        if is_valid(row, curr_square - 1):
            row[curr_square - 1] = colors[row[curr_square]]
            queue.append(curr_square - 1)
        

    answers.append("".join(row))

for answer in answers:
    print(answer, end="\n")
        