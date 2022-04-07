import random

def bubble_sort(array):
    for j in array:
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

array = [(random.randint(1,15)) for x in range(15)]
print(array)
print(bubble_sort(array))