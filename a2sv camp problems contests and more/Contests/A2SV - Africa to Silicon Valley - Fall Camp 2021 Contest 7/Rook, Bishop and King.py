r1, c1, r2, c2 = list(map(int, input().split()))
answers = []

#rook
if r1 == r2 or c1 == c2:
    answers.append(1)
else:
    answers.append(2)

#Bishop
if (r1 + c1) % 2 != (r2 + c2) % 2:
    answers.append(0)
else:
    if abs(r1 - r2) == abs(c1 - c2):
        answers.append(1)
    else:
        answers.append(2)

#King
y_diff = abs(c2 - c1)
x_diff =  abs(r2 - r1)

answers.append(min(x_diff, y_diff) + abs(y_diff - x_diff))

for answer in answers:
    print(answer, end=" ")