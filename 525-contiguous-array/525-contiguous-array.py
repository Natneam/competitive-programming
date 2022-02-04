class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Learned from https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
        """
        count = 0
        hash_map = {0 : -1}
        max_len = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in hash_map:
                max_len = max(max_len, i - hash_map[count])
            else:
                hash_map[count] = i
            
        return max_len