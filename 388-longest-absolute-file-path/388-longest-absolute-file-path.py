class Solution:
    def lengthLongestPath(self, i: str) -> int:
        max_len = 0
        depth_length = defaultdict(int)
        
        for path in i.split('\n'):
            depth = path.count('\t')
            if '.' in path:
                max_len = max(max_len, depth_length[depth] + len(path) - depth)
            else:
                depth_length[depth + 1] = depth_length[depth] + len(path) - depth + 1
        return max_len