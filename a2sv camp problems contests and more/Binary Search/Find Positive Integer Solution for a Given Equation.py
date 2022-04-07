# LINK TO THE PROBLEM => https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        for x in range(1,1001):
            min = 1
            max = 1000
            while True:
                y = (min + max)//2
                if (max <= 0 or min >= 1001) or min == max and customfunction.f(x,y) != z:
                    break
                if customfunction.f(x,y) == z:
                    result.append([x,y])
                    break
                elif customfunction.f(x,y) < z:
                    min = y+1
                else:
                    max = y - 1
        return result