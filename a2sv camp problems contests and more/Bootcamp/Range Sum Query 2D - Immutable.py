# LINK TO THE PROBLEM => https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixMatrix = []
        for row in self.matrix:
            prefixSum = [row[0]]
            for j in range(1,len(row)):
                prefixSum.append(row[j]+prefixSum[j-1])
            self.prefixMatrix.append(prefixSum)
        print(self.prefixMatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summation = 0
        for row in range(row1, row2+1):
            if col1 == 0:
                summation += self.prefixMatrix[row][col2]
            elif col2 == 0:
                return 0
            else:
                summation += self.prefixMatrix[row][col2] - self.prefixMatrix[row][col1-1]
        return summation
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
