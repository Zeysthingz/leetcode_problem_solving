# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
#
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# TODO:Solution 1: Brute Force
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         l=len(nums)
#         products_of_elements=[1]*l
#         for i in range(1,l):
#             products_of_elements[i]=products_of_elements[i-1]*nums[i-1]
#
#         right=nums[-1]
#         for i in range(l-2,-1,-1):
#             products_of_elements[i]*=right
#             right*=nums[i]
#         return products_of_elements
#

# SOLUTION 2: USING RIGHT AND LEFT ARRAY
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        left=[1]*l
        right=[1]*l
        for i in range(1,l):
            left[i]=left[i-1]*nums[i-1]
        for i in range(l-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        products_of_elements=[]
        for i in range(l):
            products_of_elements.append(left[i]*right[i])
        return products_of_elements

obj=Solution()
result=obj.productExceptSelf([1,2,3,4])
print(result)