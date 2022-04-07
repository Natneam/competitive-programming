import random

def counting_sort(arrayOfObjects, compareWith):
    # spotting maximum and minimum 
    maximum = getattr(arrayOfObjects[0], compareWith)
    minimum = getattr(arrayOfObjects[0], compareWith)
    for i in arrayOfObjects:
        if getattr(i, compareWith) < minimum:
            minimum = getattr(i, compareWith)
        if getattr(i, compareWith) > maximum:
            maximum = getattr(i, compareWith)
    # initialize an array with (maximum - minimum + 1) number of elements with empty list values 
    counterArray = [[] for x in range(minimum, maximum+1)]
    for i in arrayOfObjects:
        counterArray[getattr(i, compareWith) - minimum].append(i)
    output = []
    for x in counterArray:
        output +=  x
    return output

class Dessert:
    def __init__(self, kind ,price):
        self.kind = kind
        self.price = price

# array = [Dessert(random.choices(['a','b','c']), random.randint(10,40)) for x in range(15)]
# # for i in array:
# #     print(f'kind: {i.kind} | price: {i.price}')

# sortedArray = counting_sort(array, 'price')

# for i in sortedArray:
#     print(f'kind: {i.kind} | price: {i.price}')
