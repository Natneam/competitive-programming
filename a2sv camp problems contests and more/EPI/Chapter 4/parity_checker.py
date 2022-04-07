def parity_checker1(n: int) -> int:
    parity = 0
    while n:
        parity ^= n&1
        n = n >> 1
    return parity%2

def parity_checker2(n:int) -> int:
    parity = 0
    while n:
        parity ^= 1
        n &= n-1
    return parity

if __name__ == '__main__':
    pass