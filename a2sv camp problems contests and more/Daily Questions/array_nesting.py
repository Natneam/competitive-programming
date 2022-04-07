# LINK TO THE PROBLEM => https://leetcode.com/problems/array-nesting/

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = set()
        longest = 0
        
        def dfs(i):
            counter = 1
            s = { nums[i] }
            curr_num = nums[nums[i]]
            
            while curr_num not in s:
                s.add(curr_num)
                visited.add(curr_num)
                counter += 1
                curr_num = nums[curr_num]
            return counter
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                longest = max(longest, dfs(i))
        
        return longest
