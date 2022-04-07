def even_odd(x: list) -> list:
    start_pointer = 0
    end_pointer = len(x) - 1

    while start_pointer < end_pointer:
        # while start_pointer < len(x) and x[start_pointer] % 2 == 0:
        #     start_pointer += 1

        # while end_pointer >= 0 and x[end_pointer] % 2 == 1:
        #     end_pointer -= 1

        # if start_pointer < len(x) and end_pointer >= 0 and start_pointer < end_pointer:
        #     x[start_pointer], x[end_pointer] = x[end_pointer], x[start_pointer]
        #     start_pointer += 1
        #     end_pointer -= 1
        # else:
        #     return x
        if x[start_pointer] % 2 == 0:
            start_pointer += 1
        else:
            x[start_pointer], x[end_pointer] = x[end_pointer], x[start_pointer]
            end_pointer -= 1
    return x


print(even_odd([1, 2, 3, 4, 4, 5, 6, 13]))
