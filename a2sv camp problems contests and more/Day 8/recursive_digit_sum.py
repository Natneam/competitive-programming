# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/recursive-digit-sum/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    return helperSupDigit(str(helperSupDigit(n))*k)
    
def helperSupDigit(num):
    if len(num) == 1:
        return int(num)
    else:
        return helperSupDigit(str(sum([int(x) for x in num])))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
