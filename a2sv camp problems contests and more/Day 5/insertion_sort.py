import random

def insertion_sort(array):
    for i in range(1, len(array)):
        elementToBeInserted = array[i]
        indexToInsertAt = i
        for j in range(i-1, -1, -1):
            if elementToBeInserted < array[j]:
                array[j+1] = array[j]
                indexToInsertAt = j
        array[indexToInsertAt] = elementToBeInserted
    return array

# array = [(random.randint(1,15)) for x in range(15)]
# sortedArray = insertion_sort(array)
# # print(array)
# # print(sortedArray)
# boolean = (sorted(array)==sortedArray)
# print(boolean)