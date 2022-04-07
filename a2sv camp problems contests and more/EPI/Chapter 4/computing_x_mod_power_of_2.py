# the divisor is a power of two
from math import log2


def modules(dividend: int, divisor: int) -> int:
    divisors_log = int(log2(divisor))
    return dividend - ((dividend >> divisors_log) << divisors_log)


# print(modules(78, 64))
