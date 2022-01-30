class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        to_be_rotated = nums[len(nums) - k:]
        
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]
        
        for  i in range(len(to_be_rotated)):
            nums[i] = to_be_rotated[i]