class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def find_subsets(nums, i):
            if i == len(nums):
                return []
            
            ans = []
            vals = find_subsets(nums, i+1)
            
            ans += vals
            ans.append([nums[i]])
            for v in vals:
                ans.append([nums[i]] + v)
            return ans
        
        ans = find_subsets(nums, 0)
        ans.append([])
        return ans