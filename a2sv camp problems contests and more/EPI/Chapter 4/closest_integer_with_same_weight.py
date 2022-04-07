def closet_integer_with_same_weight(x: int) -> int:
    for i in range(63):
        if x >> i & 1 != x >> i+1 & 1:
            return x ^ ((1 << i) | (1 << (i + 1)))
    raise("All bits are 0 or 1 (overflow)")


print(closet_integer_with_same_weight(0))
