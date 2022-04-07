# 1. Assuming that keys take one of three values, reorder the array so that all objects with the
# same key appear together. The order of the subarrays is not important.

import random


def variant_1(keys, x):  # the length of the keys array is 3
    green = 0
    yellow = 0
    red = len(x) - 1

    while yellow <= red:
        if x[yellow][1] == keys[0]:
            x[yellow], x[green] = x[green], x[yellow]
            yellow += 1
            green += 1
        elif x[yellow][1] == keys[1]:
            yellow += 1
        else:
            x[yellow], x[red] = x[red], x[yellow]
            red -= 1

    return x


# print(variant_1([0, 1, 2], [[1, 0], [1, 1], [1, 2],
#       [1, 0], [1, 1], [1, 2], [1, 0], [1, 1]]))

# 1. Given an array A of n objects with keys that takes one of four values, reorder the array so
# that all objects that have the same key appear together

def variant_2(keys, x):  # keys shall contian 4 items preferably numbers or letters
    green = 0
    yellow = 0
    red = len(x) - 1
    blue = len(x) - 1

    while yellow <= red:
        if x[yellow][1] == keys[0]:
            x[yellow], x[green] = x[green], x[yellow]
            green += 1
            yellow += 1
        elif x[yellow][1] == keys[1]:
            yellow += 1
        elif x[yellow][1] == keys[2]:
            x[yellow], x[red] = x[red], x[yellow]
            red -= 1
        else:
            x[yellow], x[blue] = x[blue], x[yellow]
            blue -= 1
    return x


print(variant_2([0, 1, 2, 3], [[1, 0], [1, 1], [1, 2], [1, 3], [1, 3], [
      1, 0], [1, 1], [1, 2], [1, 3], [1, 0], [1, 1], [1, 2], [1, 3]]))

# 3. Given an array A of n objects with Boolean-valued keys, reorder the array so that objects
# that have the key false appear first. Use O(1) additional space and O(n) time


def variant_3(x):
    bool1 = 0
    bool2 = len(x) - 1
    while bool1 < bool2:  # TODO check if it should be less thank or equal
        if x[bool1]:
            x[bool2], x[bool1] = x[bool1], x[bool2]
            bool2 -= 1
        else:
            bool1 += 1
    return x

# 4. Given em array A of n objects with Boolean-valued keys, reorder the array so that objects
# that have the key false appear first. The relative ordering of objects with key true should not change.
# Use O(1) additional space and O(n) time.


def variant_4(x):
    bool1 = 0
    bool2 = len(x) - 1
    while bool1 < bool2:
        if not x[bool1]:
            x[bool1], x[bool2] = x[bool2], x[bool1]
            bool2 -= 1
        else:
            bool1 += 1
    return x
