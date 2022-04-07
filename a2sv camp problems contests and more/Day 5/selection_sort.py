import random

def selection_sort(array):
    for index in range(len(array)):
        indexOfMinimum = index
        # finding minimum
        for j in range(index,len(array)):
            if array[j] < array[indexOfMinimum]:
                indexOfMinimum = j
        array[index], array[indexOfMinimum] = array[indexOfMinimum], array[index]
    return array

# array = [random.randint(0,15) for x in range(15)]
# print(array)
# print(selection_sort(array))