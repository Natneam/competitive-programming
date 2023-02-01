class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        white_blocks = 0
        ans = float('inf')   

        for end in range(len(blocks)):
            white_blocks += 1 if blocks[end] == 'W' else 0

            if end - start + 1 == k:
                ans = min(ans, white_blocks)
                white_blocks -= 1 if blocks[start] == 'W' else 0
                start += 1
        
        return ans