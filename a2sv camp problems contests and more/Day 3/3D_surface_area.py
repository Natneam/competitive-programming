# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/3d-surface-area/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    area = len(A)*len(A[0])*2
    for i in range(len(A)):
        area += A[i][0]
        for j in range(len(A[i])-1):
            area += abs(A[i][j]-A[i][j+1])
        area += A[i][-1]
    for i in range(len(A[0])):
        area += A[0][i]
        for j in range(len(A)-1):
            area += abs(A[j][i]-A[j+1][i])
        area += A[-1][i]
    return area
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
