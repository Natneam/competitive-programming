from typing import DefaultDict
from functools import *
import sys

sys.setrecursionlimit(10000)


def solve(s,k,l,edges,letters):
    
    dp = {}
    def findAns(prev,ind,k):
        state = (prev,ind,k)
        if state in dp:
            return dp[state]

        if ind == len(s):
            return 0
            
        #change this letter
        ans = 0
        if k > 0:
            for changedLetter in letters:
                # changedLetter = chr(ord('a') + i)
                if changedLetter != s[ind]:
                    changed = findAns(changedLetter,ind +  1,k - 1) + edges[(prev,changedLetter)]
                    ans = max(ans,changed)
        
        #don't change it
        without_changing = findAns(s[ind],ind + 1,k) + edges[(prev,s[ind])]

        ans = max(ans,without_changing)
        dp[state] = ans
        return ans
    
    ans = findAns("!",0,k)
    print(ans)


def main():
    ss = input().split()
    s = ss[0]
    k = int(ss[1])

    l = int(input())
    edges = DefaultDict(int)
    letters = set()
    for i in range(l):
        edge = input().split()
        edges[(edge[0],edge[1])] = int(edge[2])
        letters.add(edge[0])
        letters.add(edge[1])
    
    solve(s,k,l,edges,letters)

main()
