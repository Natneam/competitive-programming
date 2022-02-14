class Solution:
    def lengthLongestPath(self, i: str) -> int:
        max_length = 0
        path_length = {0 : 0}
        
        for path in i.split('\n'):
            depth = path.count('\t')
            if '.' in path:
                max_length = max(max_length, path_length[depth] + len(path) - depth)
            else:
                path_length[depth + 1] = path_length[depth] + len(path) - depth + 1
        
        return max_length