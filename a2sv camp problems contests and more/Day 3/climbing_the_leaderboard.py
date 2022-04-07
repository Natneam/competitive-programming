# LINK TO THE PROBLEM => https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranks = []
    rankTracker = 1
    j = 0
    for i in range(len(ranked)):
        while j <= len(player)-1 and player[-j-1] >= ranked[i]:
            ranks.append(rankTracker)
            j += 1
        if i < len(ranked)-1 and ranked[i] != ranked[i+1]:
            rankTracker += 1
    while j < len(player):
        ranks.append(rankTracker+1)
        j+=1
    # ranks = ranks + [rankTracker+1]*(len(player)-j)
    return reversed(ranks)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
