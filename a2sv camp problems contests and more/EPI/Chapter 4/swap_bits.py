def swap_bit(number: int, i: int, j: int) -> int:
    # check if the ith and jth bit are not equal
    if ((number >> i) & 1) != ((number >> j) & 1):
        number = number ^ (1 << i)
        number = number ^ (1 << j)
    return number
