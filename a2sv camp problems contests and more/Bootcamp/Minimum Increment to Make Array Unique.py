# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-112/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        count = 0
        print(A)
        for i in range(1,len(A)):
            if A[i] <= A[i-1]:
                count += A[i-1] + 1 - A[i]
                A[i] = A[i-1] + 1
                print(count)                
                
        return count