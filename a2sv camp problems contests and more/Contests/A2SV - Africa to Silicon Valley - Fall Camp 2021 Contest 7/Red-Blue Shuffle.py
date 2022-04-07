test_cases = int(input())

answers = []

for i in range(test_cases):
    digits = int(input())
    reds = input()
    blues = input()

    larger = 0
    smaller = 0
    equal = 0
    for i in range(digits):
        if reds[i] > blues[i]:
            larger += 1
        elif reds[i] < blues[i]:
            smaller += 1
        else:
            equal += 1
    
    if larger > smaller:
        answers.append("RED")
    elif larger < smaller:
        answers.append("BLUE")
    else:
        answers.append("EQUAL")
for answer in answers:
    print(answer)