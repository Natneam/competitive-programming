class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k in counter:
            if counter[k] == 1:
                return k
        