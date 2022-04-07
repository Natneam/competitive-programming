# Write a program which takes as input an array of digits encoding a nonnegative decimal integer
# D and updates the array to represent the integer D + 1. For example, if the input is (7,2,9) then
# you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
# language that has finite-precision arithmetic.

def add_one(x: list):
    index, carry = len(x) - 1, 0
    x[index] += 1

    while index >= 0:
        x[index] += carry
        carry = 0

        if x[index] < 10:
            return x

        x[index] = 0
        carry = 1
        index -= 1

    if carry == 1:
        x.insert(0, 1)
    return x


# print(add_one([9, 9, 9]))

# Variant 1: Write a program which takes as input two strings s and f of bits encoding binary numbers
# Bs, and Bt, respectively, and returns a new string of bits representing the number Bs + Bt.

def variant_1(Bs: str, Bt: str):  # Bs and Bt are both binary encoding string
    longest = Bs if len(Bs) >= len(Bt) else Bt
    answer = ''
    carry = 0
    for i in range(-1, -len(longest)-1, -1):
        digit_Bs = 0
        digit_Bt = 0
        if len(Bs) >= abs(i):
            digit_Bs = int(Bs[i])
        if len(Bt) >= abs(i):
            digit_Bt = int(Bt[i])

        temp = digit_Bt + digit_Bs + carry

        if temp == 0:
            carry = 0
            answer += '0'
        elif temp == 1:
            carry = 0
            answer += '1'
        elif temp == 2:
            carry = 1
            answer += '0'
        else:
            carry = 1
            answer += '1'

    if carry == 1:
        answer += '1'

    return "".join(list(reversed(answer)))


print(variant_1("111", "100001"))
