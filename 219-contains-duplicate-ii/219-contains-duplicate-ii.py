class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        construct a  set from the first k elements
        if it contains duplicate, if the length of the set is less than k return True
        slide the windows, remove the 0-th element and add the element at k-th index
        if the eleemnts to be added is already inside the set just return true
        if not keep sliding the window until the end of the  array
        """
        k = k + 1
        elements = set(nums[:k])
        
        if len(nums) < k:
            return len(nums) != len(elements)
        
        if len(elements) < k:
            return True
        
        for i in range(len(nums) - k):
            elements.remove(nums[i])
            if nums[i+k] in elements:
                return True
            elements.add(nums[i+k])
        
        return False