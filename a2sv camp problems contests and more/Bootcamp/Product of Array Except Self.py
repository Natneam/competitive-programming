# LINK TO THE PROBLEM => https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProduct, postfixProduct = [1], [1]
        for i in range(1,len(nums)):
            prefixProduct.append(prefixProduct[i-1]*nums[i-1])
            postfixProduct.append(postfixProduct[i-1]*nums[len(nums) - i])
        
        return [prefixProduct[i]*postfixProduct[len(nums) - i -1] for i in range(len(nums))]
            