#LINK TO THE PROBLEM => https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3803/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        new_mat = []
        for row in range(r):
            temp_row = []
            for col in range(c):
                temp_row.append(0)
            new_mat.append(temp_row)
        
        count = 0
        row_num = 0
        for row in mat:
            for item in row:
                new_mat[row_num][count%c] = item
                count += 1
                if count % c == 0: row_num += 1
        
        return new_mat
