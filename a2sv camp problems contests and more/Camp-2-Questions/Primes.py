from math import  sqrt

number = int(input()) - 2

if int(sqrt(number)) ** 2 == number:
    print(-1)
else:
    is_prime = True
    for i in range(2, int(sqrt(number))):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"2 {number}")
    else:
        print(-1)