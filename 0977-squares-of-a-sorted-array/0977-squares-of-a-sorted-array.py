class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return [x*x for x in sorted(nums, key=abs)]