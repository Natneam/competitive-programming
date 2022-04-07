# LINK TO THE QUESTION => https://www.hackerrank.com/contests/a2sv2/challenges/bon-appetit

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anaEats = sum(bill[0:k] + bill[k+1:])/2
    bnet = int(b - anaEats)
    if bnet == 0:
        print('Bon Appetit')
    else:
        print(bnet)
    
if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)