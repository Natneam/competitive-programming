import random

def counting_sort(array):
    # spotting maximum and minimum 
    maximum = array[0]
    minimum = array[0]
    for i in array:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    # initialize an array with (maximum - minimum + 1) number 0 elements 
    counterArray = [0 for x in range(minimum, maximum+1)]
    for i in array:
        counterArray[i-minimum] += 1
    output = []
    for (i,x) in enumerate(counterArray):
        output +=  [i + minimum]*x
    return output

# array = [(random.randint(1,15)) for x in range(15)]
# print(array)
# print(counting_sort(array)==sorted(array))