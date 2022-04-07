# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/countingsort2/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    # initializing the counting array
    countingArray = [0 for x in range(100)]
    sortedArray = []
    for i in arr:
        countingArray[i] += 1
    print(countingArray)
    for index,value in enumerate(countingArray):
        sortedArray += [index] * value
    return sortedArray
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
