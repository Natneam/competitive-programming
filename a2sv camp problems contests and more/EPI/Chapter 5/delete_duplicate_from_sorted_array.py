# Write a program which takes as input a sorted array and updates it so that all duplicates have been
# removed and the remaining elements have been shifted left to fill the emptied indices. Return the
# number of valid elements. Many languages have library functions for performing this operationyou cannot use these functions.

def delete_duplicate(lst: list) -> list:
    write_index = 1

    for i in range(1,len(lst)):
        if lst[write_index - 1] != lst[i]:
            lst[write_index] = lst[i]
            write_index += 1
    return lst

print(delete_duplicate([-1,-1,-1,1,2,3,4,4,4,4,5,5,6,6]))
