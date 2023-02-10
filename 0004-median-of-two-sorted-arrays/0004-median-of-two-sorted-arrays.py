class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # time : O(n + m)
        # space : O(n + m)
        nums = []

        index_1 = 0
        index_2 = 0

        while index_1 < len(nums1) or index_2 < len(nums2):
            if index_1 >= len(nums1):
                nums.append(nums2[index_2])
                index_2 += 1
            elif index_2 >= len(nums2):
                nums.append(nums1[index_1])
                index_1 += 1
            else:
                if nums1[index_1] <= nums2[index_2]:
                    nums.append(nums1[index_1])
                    index_1  += 1
                else:
                    nums.append(nums2[index_2])
                    index_2 += 1
        n = len(nums)
        if n % 2 == 0:
            return (nums[n//2 - 1] + nums[n//2]) / 2
        return nums[n//2]
