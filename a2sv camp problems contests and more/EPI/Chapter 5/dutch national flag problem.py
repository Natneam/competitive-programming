def dutch_flag_partition(x: list, i: int) -> list:
    # start_index = 0
    # end_index = len(x) - 1
    pivot = x[i]

    # while start_index < end_index:
    #     if x[start_index] < pivot:
    #         start_index += 1
    #     else:
    #         x[start_index], x[end_index] = x[end_index], x[start_index]
    #         end_index -= 1

    # end_index = len(x) - 1
    # while start_index < end_index:
    #     if x[start_index] == pivot:
    #         start_index += 1
    #     else:
    #         x[start_index], x[end_index] = x[end_index], x[start_index]
    #         end_index -= 1

    # more beautiful way of solving it
    smaller = 0
    equal = 0
    larger = len(x) - 1

    while equal < larger:
        if x[equal] < pivot:
            x[smaller], x[equal] = x[equal], x[smaller]
            smaller += 1
            equal += 1
        elif x[equal] == pivot:
            equal += 1
        else:
            x[larger], x[equal] = x[equal], x[larger]
            larger -= 1

    return x


print(dutch_flag_partition([1, 3, 87, 4, 7, 5, 4, 4, 4], 3))
