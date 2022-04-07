def right_propagate_rightmost_set_bit(x: int) -> int:
    # copy_x = x
    # count = 0
    # while copy_x & ~((~0) << 1) == 0:
    #     copy_x = copy_x >> 1
    #     count += 1
    # return x | ~((~0) << count)
    return x | (x-1)


test_num = 80
assert bin(test_num), bin(right_propagate_rightmost_set_bit(test_num))
