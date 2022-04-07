# LINK TO THE PROBLEM => https://leetcode.com/problems/largest-perimeter-triangle/submissions/

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # sorting the array
        A.sort()
        A.reverse()
        
        # sorting the array using buble sort
        # for j in range(len(A)):
        #     for i in range(len(A)-j-1):
        #         if A[i] < A[i+1]: # sorting in reverse order
        #             A[i], A[i+1] = A[i+1], A[i]      
        
        
        # every triangle has a non-zero area if the largest side is smaller than
        # the sum of two smaller sides (in fact, it is called triangle if 
        # it satisfies this condition )
        for i in range(len(A)-2):
            side1 = A[i]
            side2 = A[i+1]
            side3 = A[i+2]
            
            if side1 < (side2 + side3):
                return side1+side2+side3
        return 0