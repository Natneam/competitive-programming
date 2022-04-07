# LINK TO THE PROBELM => https://www.hackerrank.com/challenges/quicksort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    less = []
    greater = []
    for i in arr:
        if i < p:
            less.append(i)
        elif i > p:
            greater.append(i)
    return less + [p] + greater
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
