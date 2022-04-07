# LINK TO THE PROBLEM => https://www.hackerrank.com/contests/a2sv-contest-3/challenges/jesse-and-cookies/problem

#!/bin/python3

import os
import sys
import heapq

#
# Complete the cookies function below.
#
def cookies(k, A):
    heapq.heapify(A)
    counter = 0
    try:
        small1 = heapq.heappop(A)
        if small1 >= k:
            return counter
        small2 = heapq.heappop(A)
    except:
        return -1
    
    while small1 < k:
        heapq.heappush(A, 1*small1 + 2*small2)
        counter += 1
        try:
            small1 = heapq.heappop(A)
            if small1 >= k:
                return counter
            small2 = heapq.heappop(A)
        except:
            return -1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
