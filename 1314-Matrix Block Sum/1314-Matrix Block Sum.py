class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefix_matrix = [[0]*(len(mat[0]) + 1)]
        for i in range(len(mat)):
            prefix_matrix.append([0])
            for j in range(len(mat[0])):
                arr = prefix_matrix[i + 1]
                arr.append(arr[-1] + mat[i][j])
        
        for i in range(1, len(prefix_matrix)):
            for j in range(len(prefix_matrix[0])):
                prefix_matrix[i][j] += prefix_matrix[i - 1][j]

        ans = []
        for i in range(len(mat)):
            ans.append([])
            y_s = [max(0, i - k), min(len(mat) - 1, i + k)]
            for j in range(len(mat[0])):
                x_s = [max(0, j - k), min(len(mat[0]) - 1, j + k)]
                ans[i].append(prefix_matrix[y_s[1] + 1][x_s[1] + 1] - prefix_matrix[y_s[1] + 1][x_s[0]] - prefix_matrix[y_s[0]][x_s[1] + 1] + prefix_matrix[y_s[0]][x_s[0]])
        return ans
        